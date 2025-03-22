<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl, FormMessage } from '@/components/ui/form'
import { Input } from '@/components/ui/input'
import { Separator } from '@/components/ui/separator'

defineProps<{
    isFieldDirty: any
}>()
</script>

<template>
    <div class="grid grid-cols-2 gap-4">
        <div class="space-y-1 col-span-2">
            <span class="text-xl font-medium">Segurança</span>
            <Separator />
        </div>

        <FormField v-slot="{ componentField }" name="password" :validate-on-blur="!isFieldDirty">
            <FormItem class="col-span-2 md:col-span-1">
                <FormLabel>Senha</FormLabel>
                <FormControl>
                    <Input
                        autocomplete="off"
                        type="password"
                        placeholder="Insira a senha"
                        v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>
        <FormField
            v-slot="{ componentField }"
            name="confirmPassword"
            :validate-on-blur="!isFieldDirty">
            <FormItem class="col-span-2 md:col-span-1">
                <FormLabel>Confirmar Senha</FormLabel>
                <FormControl>
                    <Input
                        autocomplete="off"
                        type="password"
                        placeholder="Insira a confirmação da senha"
                        v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>
    </div>
</template>
