import { passwordSchema, receptionistSchema } from '@/lib/schema'
import { toTypedSchema } from '@vee-validate/zod'
import * as z from 'zod'

const schema = receptionistSchema
    .merge(passwordSchema)
    .refine((data) => data.password === data.confirmPassword, {
        message: 'As senhas devem ser iguais',
        path: ['confirmPassword']
    })

export const receptionistDataSchema: ReturnType<typeof toTypedSchema> = toTypedSchema(schema)
export type ReceptionistDataSchema = z.infer<typeof schema>
