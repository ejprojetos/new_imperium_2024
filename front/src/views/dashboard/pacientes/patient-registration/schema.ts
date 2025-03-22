import { passwordSchema, patientSchema } from '@/lib/schema'
import { toTypedSchema } from '@vee-validate/zod'
import * as z from 'zod'

const schema = patientSchema
    .merge(passwordSchema)
    .refine((data) => data.password === data.confirmPassword, {
        message: 'As senhas devem ser iguais',
        path: ['confirmPassword']
    })

export const patientDataSchema: ReturnType<typeof toTypedSchema> = toTypedSchema(schema)
export type PatientDataSchema = z.infer<typeof schema>
