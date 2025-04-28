import { doctorSchema } from '@/lib/schema'
import { toTypedSchema } from '@vee-validate/zod'
import * as z from 'zod'

const schema = doctorSchema

export const doctorDataSchema: ReturnType<typeof toTypedSchema> = toTypedSchema(schema)
export type DoctorDataSchema = z.infer<typeof schema>
