<script setup lang="ts">
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card'
import { FormField, FormItem, FormLabel, FormControl, FormMessage } from '@/components/ui/form'
import { Checkbox } from '@/components/ui/checkbox'
import { RadioGroup, RadioGroupItem } from '@/components/ui/radio-group'
import { weekDays, turns } from '../data'

defineProps<{
    isEditMode: boolean
    isFieldDirty: any
}>()
</script>

<template>
    <Card>
        <CardHeader>
            <CardTitle>Expediente</CardTitle>
            <CardDescription>Configurações de horários e disponibilidade</CardDescription>
            <span
                v-if="isEditMode"
                class="absolute right-8 bg-yellow-300/40 border border-yellow-700 rounded-full px-2 py-0.5 font-medium text-sm">
                Modo edição
            </span>
        </CardHeader>
        <CardContent class="grid gap-4">
            <FormField name="workDays">
                <FormItem>
                    <FormLabel class="text-base">Dias da semana</FormLabel>
                    <div class="flex flex-wrap gap-3">
                        <FormField
                            v-for="day in weekDays"
                            :key="day.id"
                            v-slot="{ value, handleChange }"
                            name="workDays">
                            <FormItem>
                                <FormControl>
                                    <Checkbox
                                        :disabled="!isEditMode"
                                        :model-value="value.includes(day.id)"
                                        @update:model-value="
                                            (checked) => {
                                                const newValue = checked
                                                    ? [...value, day.id]
                                                    : value.filter(
                                                          (dayId: string) => dayId !== day.id
                                                      )
                                                handleChange(newValue)
                                            }
                                        "
                                        :label="day.label" />
                                </FormControl>
                            </FormItem>
                        </FormField>
                    </div>
                    <FormMessage />
                </FormItem>
            </FormField>
            <FormField name="turns">
                <FormItem>
                    <FormLabel class="text-base">Turnos</FormLabel>
                    <div class="flex flex-wrap gap-3">
                        <FormField
                            v-for="turn in turns"
                            :key="turn.id"
                            v-slot="{ value, handleChange }"
                            name="turns">
                            <FormItem>
                                <FormControl>
                                    <Checkbox
                                        :disabled="!isEditMode"
                                        :model-value="value.includes(turn.id)"
                                        @update:model-value="
                                            (checked) => {
                                                const newValue = checked
                                                    ? [...value, turn.id]
                                                    : value.filter((t: string) => t !== turn.id)
                                                handleChange(newValue)
                                            }
                                        "
                                        :label="turn.label" />
                                </FormControl>
                            </FormItem>
                        </FormField>
                    </div>
                    <FormMessage />
                </FormItem>
            </FormField>

            <FormField v-slot="{ componentField }" type="radio" name="availableForShift">
                <FormItem class="space-y-3">
                    <FormLabel>Disponibilidade para plantão</FormLabel>

                    <FormControl>
                        <RadioGroup
                            class="flex flex-col space-y-1"
                            v-bind="componentField"
                            :disabled="!isEditMode">
                            <FormItem class="flex items-center space-y-0 gap-x-3">
                                <FormControl>
                                    <RadioGroupItem value="no" />
                                </FormControl>
                                <FormLabel class="font-normal">Sim</FormLabel>
                            </FormItem>
                            <FormItem class="flex items-center space-y-0 gap-x-3">
                                <FormControl>
                                    <RadioGroupItem value="yes" />
                                </FormControl>
                                <FormLabel class="font-normal">Não</FormLabel>
                            </FormItem>
                        </RadioGroup>
                    </FormControl>
                    <FormMessage />
                </FormItem>
            </FormField>
        </CardContent>
    </Card>
</template>
