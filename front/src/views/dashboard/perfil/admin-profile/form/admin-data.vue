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
            <span class="text-xl font-medium">Dados principais</span>
            <Separator />
        </div>

        <FormField v-slot="{ componentField }" name="fullname" :validate-on-blur="!isFieldDirty">
            <FormItem class="col-span-2 md:col-span-1">
                <FormLabel>Nome da clínica</FormLabel>
                <FormControl>
                    <Input
                        type="text"
                        placeholder="Insira o nome da clínica"
                        v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>

        <FormField v-slot="{ componentField }" name="fullname" :validate-on-blur="!isFieldDirty">
            <FormItem class="col-span-2 md:col-span-1">
                <FormLabel>Nome do responsável</FormLabel>
                <FormControl>
                    <Input
                        type="text"
                        placeholder="Insira o seu nome completo"
                        v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>

        <FormField v-slot="{ componentField }" name="cnpj" :validate-on-blur="!isFieldDirty">
            <FormItem class="col-span-2 md:col-span-1">
                <FormLabel>RG do responsável</FormLabel>
                <FormControl>
                    <Input
                        placeholder="00.000.000-0"
                        v-maska="'##.###.###-#'"
                        v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>

        <FormField v-slot="{ componentField }" name="cpf" :validate-on-blur="!isFieldDirty">
            <FormItem class="col-span-2 md:col-span-1">
                <FormLabel>CPF</FormLabel>
                <FormControl>
                    <Input
                        placeholder="000.000.000-00"
                        v-maska="'###.###.###-##'"
                        v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>

        <FormField v-slot="{ componentField }" name="cnpj" :validate-on-blur="!isFieldDirty">
            <FormItem class="col-span-2 md:col-span-1">
                <FormLabel>CNPJ</FormLabel>
                <FormControl>
                    <Input
                        placeholder="00.000.000/0000-00"
                        v-maska="'##.###.###/####-##'"
                        v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>
    </div>
</template>
