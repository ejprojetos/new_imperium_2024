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
    <div class="grid grid-cols-4 md:grid-cols-3 gap-4">
        <div class="space-y-1 col-span-4 md:col-span-3">
            <span class="text-xl font-medium">Endereço</span>
            <Separator />
        </div>

        <div class="col-span-4 md:col-span-3">
            <FormField
                v-slot="{ componentField }"
                name="address.zipCode"
                :validate-on-blur="!isFieldDirty">
                <FormItem class="md:w-[calc(33%-0.5rem)]">
                    <FormLabel>CEP</FormLabel>
                    <FormControl>
                        <Input
                            type="text"
                            placeholder="Insira o CEP"
                            v-maska="'#####-###'"
                            v-bind="componentField" />
                    </FormControl>

                    <FormMessage />
                </FormItem>
            </FormField>
        </div>

        <FormField
            v-slot="{ componentField }"
            name="address.country"
            :validate-on-blur="!isFieldDirty">
            <FormItem class="col-span-2 md:col-span-1">
                <FormLabel>País</FormLabel>
                <FormControl>
                    <Input type="text" placeholder="Insira o país" v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>

        <FormField
            v-slot="{ componentField }"
            name="address.state"
            :validate-on-blur="!isFieldDirty">
            <FormItem class="col-span-2 md:col-span-1">
                <FormLabel>Estado</FormLabel>
                <FormControl>
                    <Input
                        maxlength="2"
                        type="text"
                        placeholder="Insira o estado"
                        v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>

        <FormField
            v-slot="{ componentField }"
            name="address.city"
            :validate-on-blur="!isFieldDirty">
            <FormItem class="col-span-2 md:col-span-1">
                <FormLabel>Cidade</FormLabel>
                <FormControl>
                    <Input type="text" placeholder="Insira a cidade" v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>

        <FormField
            v-slot="{ componentField }"
            name="address.neighborhood"
            :validate-on-blur="!isFieldDirty">
            <FormItem class="col-span-2 md:col-span-1">
                <FormLabel>Bairro</FormLabel>
                <FormControl>
                    <Input type="text" placeholder="Insira a cidade" v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>

        <FormField
            v-slot="{ componentField }"
            name="address.street"
            :validate-on-blur="!isFieldDirty">
            <FormItem class="col-span-3 md:col-span-1">
                <FormLabel>Logradouro</FormLabel>
                <FormControl>
                    <Input type="text" placeholder="Insira o lagradouro" v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>

        <FormField
            v-slot="{ componentField }"
            name="address.number"
            :validate-on-blur="!isFieldDirty">
            <FormItem>
                <FormLabel>Número</FormLabel>
                <FormControl>
                    <Input type="text" placeholder="Insira o número" v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>
    </div>
</template>
