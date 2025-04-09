import { adminSchema } from '@/lib/schema'
import { toTypedSchema } from '@vee-validate/zod'
import * as z from 'zod'

const schema = adminSchema

export const adminDataSchema: ReturnType<typeof toTypedSchema> = toTypedSchema(schema)
export type AdminDataSchema = z.infer<typeof schema>
