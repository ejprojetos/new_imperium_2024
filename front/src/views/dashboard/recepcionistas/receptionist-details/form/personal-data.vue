<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl, FormMessage } from '@/components/ui/form'
import { Input } from '@/components/ui/input'
import { Separator } from '@/components/ui/separator'
import {
    Select,
    SelectContent,
    SelectGroup,
    SelectItem,
    SelectTrigger,
    SelectValue
} from '@/components/ui/select'
import { vMaska } from 'maska/vue'

defineProps<{
    isFieldDirty: any
}>()
</script>

<template>
    <div class="grid grid-cols-2 gap-4">
        <div class="space-y-1 col-span-2">
            <span class="text-xl font-medium">Informações básicas</span>
            <Separator />
        </div>

        <FormField v-slot="{ componentField }" name="fullname" :validate-on-blur="!isFieldDirty">
            <FormItem class="col-span-2 md:col-span-1">
                <FormLabel>Nome Completo</FormLabel>
                <FormControl>
                    <Input
                        type="text"
                        placeholder="Insira o seu nome completo"
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

        <FormField v-slot="{ componentField }" name="dateOfBirth" :validate-on-blur="!isFieldDirty">
            <FormItem class="col-span-2 md:col-span-1">
                <FormLabel>Data de nascimento</FormLabel>
                <FormControl>
                    <Input
                        placeholder="DD/MM/YYYY"
                        v-maska="'##/##/####'"
                        v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>

        <FormField v-slot="{ componentField }" name="gender">
            <FormItem class="col-span-2 md:col-span-1">
                <FormLabel>Gênero</FormLabel>

                <Select v-bind="componentField">
                    <FormControl>
                        <SelectTrigger class="w-full">
                            <SelectValue placeholder="Select a option" />
                        </SelectTrigger>
                    </FormControl>
                    <SelectContent>
                        <SelectGroup>
                            <SelectItem value="Masculino">Masculino</SelectItem>
                            <SelectItem value="Feminino">Feminino</SelectItem>
                            <SelectItem value="Outro">Outro</SelectItem>
                        </SelectGroup>
                    </SelectContent>
                </Select>

                <FormMessage />
            </FormItem>
        </FormField>
    </div>
</template>
