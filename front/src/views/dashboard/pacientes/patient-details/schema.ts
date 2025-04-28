import { toTypedSchema } from '@vee-validate/zod'
import * as z from 'zod'

const fullnameSchema = z
    .string()
    .min(5, 'O nome completo deve ter pelo menos 5 caracteres')
    .refine((value) => value.trim().split(/\s+/).length >= 2, {
        message: 'O nome completo deve incluir nome e sobrenome'
    })

const cpfSchema = z.string().regex(/^\d{3}\.\d{3}\.\d{3}-\d{2}$/, 'CPF inválido')

const dateOfBirthSchema = z
    .string()
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

const schema = z.object({
    fullname: fullnameSchema,
    cpf: cpfSchema,
    dateOfBirth: dateOfBirthSchema,
    gender: z.enum(['Masculino', 'Feminino', 'Outro'], {
        message: 'Gênero inválido. Escolha entre Masculino, Feminino ou Outro'
    }),
    address: z.object({
        zipCode: z.string().regex(/^\d{5}-\d{3}$/, 'CEP inválido'),
        country: z.string().min(3, 'País deve ter pelo menos 3 caracteres'),
        state: z.string().max(2, 'Insira a sígla').nonempty('Estado não pode estar vazio'),
        city: z.string().nonempty('Cidade não pode estar vazia'),
        neighborhood: z.string().nonempty('Bairro não pode estar vazio'),
        street: z.string().nonempty('Rua não pode estar vazia'),
        number: z.string().nonempty('Número não pode estar vazio')
    }),
    email: z.string().email('E-mail inválido'),
    phone: z.string().regex(/^\(\d{2}\) \d{4,5}-\d{4}$/, 'Telefone inválido')
})

export const patientDataSchema: ReturnType<typeof toTypedSchema> = toTypedSchema(schema)
export type PatientDataSchema = z.infer<typeof schema>
