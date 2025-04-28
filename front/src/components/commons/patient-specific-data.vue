<script setup lang="ts">
import { FormControl, FormField, FormItem, FormMessage } from '../ui/form'
import { Input } from '../ui/input'

defineProps<{
    isFieldDirty: any
}>()
</script>

<template>
    <div class="grid grid-cols-2 md:grid-cols-2 gap-4">
        <div class="space-y-1 col-span-2">
            <span class="text-xl font-medium">Informações importantes para o médico</span>
            <Separator />
        </div>

        <FormField v-slot="{ componentField }" name="crm" :validate-on-blur="!isFieldDirty">
            <FormItem class="">
                <FormLabel>Alergias:</FormLabel>
                <FormControl>
                    <Input
                        type="text"
                        placeholder="Insira as alergias"
                        maxlength="11"
                        v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>
        <FormField v-slot="{ componentField }" name="crm" :validate-on-blur="!isFieldDirty">
            <FormItem class="">
                <FormLabel>Problemas recorrentes:</FormLabel>
                <FormControl>
                    <Input
                        type="text"
                        placeholder="Insira os problemas"
                        maxlength="11"
                        v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>
    </div>
</template>
