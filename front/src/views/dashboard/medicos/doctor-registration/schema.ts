import { toTypedSchema } from '@vee-validate/zod'
import * as z from 'zod'

const fullnameSchema = z
    .string({
        required_error: 'Campo obrigatório'
    })
    .min(5, 'O nome completo deve ter pelo menos 5 caracteres')
    .refine((value) => value.trim().split(/\s+/).length >= 2, {
        message: 'O nome completo deve incluir nome e sobrenome'
    })

const cpfSchema = z
    .string({
        required_error: 'Campo obrigatório'
    })
    .regex(/^\d{3}\.\d{3}\.\d{3}-\d{2}$/, 'CPF inválido')

const dateOfBirthSchema = z
    .string({
        required_error: 'Campo obrigatório'
    })
    .regex(/^\d{2}\/\d{2}\/\d{4}$/, 'Data de nascimento inválida. Use o formato DD/MM/YYYY')
    .refine(
        (date) => {
            const [day, month, year] = date.split('/').map(Number)
            const birthDate = new Date(year, month - 1, day)
            const today = new Date()
            const age = today.getFullYear() - birthDate.getFullYear()
            const monthDiff = today.getMonth() - birthDate.getMonth()
            const dayDiff = today.getDate() - birthDate.getDate()

            if (monthDiff < 0 || (monthDiff === 0 && dayDiff < 0)) {
                return age - 1 >= 14
            }
            return age >= 14
        },
        {
            message: 'Data de nascimento deve ser maior que 13 anos'
        }
    )

const MAX_FILE_SIZE = 5 * 1024 * 1024 // 5MB
const ACCEPTED_FILE_TYPES = ['image/jpeg', 'image/png', 'image/jpg', 'application/pdf']

const passwordSchema = z
    .string({
        required_error: 'Campo obrigatório'
    })
    .min(6, 'A senha deve ter pelo menos 6 caracteres')
    .regex(/[A-Z]/, 'Password must contain at least one uppercase letter')
    .regex(/[a-z]/, 'Password must contain at least one lowercase letter')
    .regex(/[0-9]/, 'Password must contain at least one number')

const schema: z.ZodSchema = z
    .object({
        fullname: fullnameSchema,
        cpf: cpfSchema,
        dateOfBirth: dateOfBirthSchema,
        gender: z.enum(['Masculino', 'Feminino', 'Outro'], {
            message: 'Gênero inválido. Escolha entre Masculino, Feminino ou Outro'
        }),
        address: z.object({
            zipCode: z
                .string({
                    required_error: 'Campo obrigatório'
                })
                .regex(/^\d{5}-\d{3}$/, 'CEP inválido'),
            country: z
                .string({
                    required_error: 'Campo obrigatório'
                })
                .min(3, 'País deve ter pelo menos 3 caracteres'),
            state: z
                .string({
                    required_error: 'Campo obrigatório'
                })
                .max(2, 'Insira a sígla')
                .nonempty('Estado não pode estar vazio'),
            city: z
                .string({
                    required_error: 'Campo obrigatório'
                })
                .nonempty('Cidade não pode estar vazia'),
            neighborhood: z
                .string({
                    required_error: 'Campo obrigatório'
                })
                .nonempty('Bairro não pode estar vazio'),
            street: z
                .string({
                    required_error: 'Campo obrigatório'
                })
                .nonempty('Rua não pode estar vazia'),
            number: z
                .string({
                    required_error: 'Campo obrigatório'
                })
                .nonempty('Número não pode estar vazio')
        }),
        email: z
            .string({
                required_error: 'Campo obrigatório'
            })
            .email('E-mail inválido'),
        phone: z
            .string({
                required_error: 'Campo obrigatório'
            })
            .regex(/^\(\d{2}\) \d{4,5}-\d{4}$/, 'Telefone inválido'),
        // specialty: z.string(),
        formation: z.string({
            required_error: 'Campo obrigatório'
        }),
        crm: z
            .string({
                required_error: 'Campo obrigatório'
            })
            .nonempty('CRM não pode estar vazio'),
        password: passwordSchema,
        confirmPassword: z.string({
            required_error: 'Campo obrigatório'
        }),
        file: z
            .instanceof(File)
            .refine((file) => file.size <= MAX_FILE_SIZE, {
                message: 'O arquivo deve ter no máximo 5MB'
            })
            .refine((file) => ACCEPTED_FILE_TYPES.includes(file.type), {
                message: 'Formato inválido. Apenas PNG, JPG, JPEG e PDF são permitidos.'
            })
            .optional()
    })
    .refine((data) => data.password === data.confirmPassword, {
        message: 'As senhas devem ser iguais',
        path: ['confirmPassword']
    })

export const doctorDataSchema: ReturnType<typeof toTypedSchema> = toTypedSchema(schema)
export type DoctorDataSchema = z.infer<typeof schema>
