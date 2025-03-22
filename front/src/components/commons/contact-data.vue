<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl, FormMessage } from '@/components/ui/form'
import { Input } from '@/components/ui/input'
import { Separator } from '@/components/ui/separator'
import { vMaska } from 'maska/vue'

defineProps<{
    isFieldDirty: any
}>()
</script>

<template>
    <div class="grid grid-cols-2 gap-4">
        <div class="space-y-1 col-span-2">
            <span class="text-xl font-medium">Contato</span>
            <Separator />
        </div>

        <FormField v-slot="{ componentField }" name="email" :validate-on-blur="!isFieldDirty">
            <FormItem class="col-span-2 md:col-span-1">
                <FormLabel>Email</FormLabel>
                <FormControl>
                    <Input
                        autocomplete="off"
                        type="email"
                        placeholder="Insira o email"
                        v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>
        <FormField v-slot="{ componentField }" name="phone" :validate-on-blur="!isFieldDirty">
            <FormItem class="col-span-2 md:col-span-1">
                <FormLabel>Telefone</FormLabel>
                <FormControl>
                    <Input
                        id="phone"
                        placeholder="Insara o número de telefone"
                        v-maska="'(##) #####-####'"
                        v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>
    </div>
</template>
