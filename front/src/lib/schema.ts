import { z } from 'zod'

const stringRequiredError = z.string({
    required_error: 'Campo obrigatório'
})
const fullnameSchema = stringRequiredError
    .min(5, 'O nome completo deve ter pelo menos 5 caracteres')
    .refine((value) => value.trim().split(/\s+/).length >= 2, {
        message: 'O nome completo deve incluir nome e sobrenome'
    })

const cpfSchema = stringRequiredError.regex(/^\d{3}\.\d{3}\.\d{3}-\d{2}$/, 'CPF inválido')

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

const passwordValidationSchema = z
    .string({
        required_error: 'Campo obrigatório'
    })
    .min(6, 'A senha deve ter pelo menos 6 caracteres')
    .regex(/[A-Z]/, 'Password must contain at least one uppercase letter')
    .regex(/[a-z]/, 'Password must contain at least one lowercase letter')
    .regex(/[0-9]/, 'Password must contain at least one number')

export const passwordSchema = z.object({
    password: passwordValidationSchema,
    confirmPassword: z.string({
        required_error: 'Campo obrigatório'
    })
})

const addressSchema = z.object({
    zipCode: stringRequiredError.regex(/^\d{5}-\d{3}$/, 'CEP inválido'),
    country: stringRequiredError.min(3, 'País deve ter pelo menos 3 caracteres'),
    state: stringRequiredError.max(2, 'Insira a sígla').nonempty('Estado não pode estar vazio'),
    city: stringRequiredError.nonempty('Cidade não pode estar vazia'),
    neighborhood: stringRequiredError.nonempty('Bairro não pode estar vazio'),
    street: stringRequiredError.nonempty('Rua não pode estar vazia'),
    number: stringRequiredError.nonempty('Número não pode estar vazio')
})

export const receptionistSchema = z.object({
    fullname: fullnameSchema,
    cpf: cpfSchema,
    dateOfBirth: dateOfBirthSchema,
    gender: z.enum(['Masculino', 'Feminino', 'Outro'], {
        message: 'Gênero inválido. Escolha entre Masculino, Feminino ou Outro'
    }),
    address: addressSchema,
    email: stringRequiredError.email('E-mail inválido'),
    phone: stringRequiredError.regex(/^\(\d{2}\) \d{4,5}-\d{4}$/, 'Telefone inválido'),
    workDays: z.array(stringRequiredError).refine((value) => value.some((item) => item), {
        message: 'Você precisa selecionar uma opção'
    }),
    turns: z.array(stringRequiredError).refine((value) => value.some((item) => item), {
        message: 'Você precisa selecionar uma opção'
    }),
    availableForShift: z.enum(['yes', 'no'], {
        message: 'Disponibilidade para plantão é obrigatória'
    })
})

export const patientSchema = z.object({
    fullname: fullnameSchema,
    cpf: cpfSchema,
    dateOfBirth: dateOfBirthSchema,
    gender: z.enum(['Masculino', 'Feminino', 'Outro'], {
        message: 'Gênero inválido. Escolha entre Masculino, Feminino ou Outro'
    }),
    address: addressSchema,
    email: stringRequiredError.email('E-mail inválido'),
    phone: stringRequiredError.regex(/^\(\d{2}\) \d{4,5}-\d{4}$/, 'Telefone inválido')
})
