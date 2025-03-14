<script setup lang="ts">
import { FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form'
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
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
    isEditMode: boolean
    isFieldDirty: any
}>()
</script>

<template>
    <Card>
        <CardHeader>
            <CardTitle>Dados Pessoais</CardTitle>
            <CardDescription>Dados de identificação e contato do profissional</CardDescription>

            <span
                v-if="isEditMode"
                class="absolute right-8 bg-yellow-300/40 border border-yellow-700 rounded-full px-2 py-0.5 font-medium text-sm">
                Modo edição
            </span>
        </CardHeader>
        <CardContent class="flex flex-col gap-6">
            <div class="flex flex-col gap-3">
                <div class="grid grid-cols-2 gap-4">
                    <FormField
                        v-slot="{ componentField }"
                        name="fullname"
                        :validate-on-blur="!isFieldDirty">
                        <FormItem>
                            <FormLabel>Nome Completo</FormLabel>
                            <FormControl>
                                <Input
                                    type="text"
                                    placeholder="Insira o seu nome completo"
                                    :disabled="!isEditMode"
                                    v-bind="componentField" />
                            </FormControl>

                            <FormMessage />
                        </FormItem>
                    </FormField>
                    <FormField
                        v-slot="{ componentField }"
                        name="cpf"
                        :validate-on-blur="!isFieldDirty">
                        <FormItem>
                            <FormLabel>CPF</FormLabel>
                            <FormControl>
                                <Input
                                    placeholder="000.000.000-00"
                                    v-maska="'###.###.###-##'"
                                    :disabled="!isEditMode"
                                    v-bind="componentField" />
                            </FormControl>

                            <FormMessage />
                        </FormItem>
                    </FormField>
                </div>

                <div class="grid grid-cols-2 gap-4">
                    <FormField
                        v-slot="{ componentField }"
                        name="dateOfBirth"
                        :validate-on-blur="!isFieldDirty">
                        <FormItem>
                            <FormLabel>Data de nascimento</FormLabel>
                            <FormControl>
                                <Input
                                    placeholder="DD/MM/YYYY"
                                    v-maska="'##/##/####'"
                                    :disabled="!isEditMode"
                                    v-bind="componentField" />
                            </FormControl>

                            <FormMessage />
                        </FormItem>
                    </FormField>

                    <FormField v-slot="{ componentField }" name="gender">
                        <FormItem>
                            <FormLabel>Email</FormLabel>

                            <Select v-bind="componentField">
                                <FormControl>
                                    <SelectTrigger class="w-full" :disabled="!isEditMode">
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
            </div>
            <div class="grid grid-cols-3 gap-4">
                <div class="space-y-1 col-span-3">
                    <span class="text-xl font-medium">Endereço</span>
                    <Separator />
                </div>
                <div class="col-span-3">
                    <FormField
                        v-slot="{ componentField }"
                        name="address.zipCode"
                        :validate-on-blur="!isFieldDirty">
                        <FormItem>
                            <FormLabel>CEP</FormLabel>
                            <FormControl>
                                <Input
                                    type="text"
                                    placeholder="Insira o CEP"
                                    :disabled="!isEditMode"
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
                    <FormItem>
                        <FormLabel>País</FormLabel>
                        <FormControl>
                            <Input
                                type="text"
                                placeholder="Insira o país"
                                :disabled="!isEditMode"
                                v-bind="componentField" />
                        </FormControl>

                        <FormMessage />
                    </FormItem>
                </FormField>

                <FormField
                    v-slot="{ componentField }"
                    name="address.state"
                    :validate-on-blur="!isFieldDirty">
                    <FormItem>
                        <FormLabel>Estado</FormLabel>
                        <FormControl>
                            <Input
                                type="text"
                                placeholder="Insira o estado"
                                :disabled="!isEditMode"
                                v-bind="componentField" />
                        </FormControl>

                        <FormMessage />
                    </FormItem>
                </FormField>

                <FormField
                    v-slot="{ componentField }"
                    name="address.city"
                    :validate-on-blur="!isFieldDirty">
                    <FormItem>
                        <FormLabel>Cidade</FormLabel>
                        <FormControl>
                            <Input
                                type="text"
                                placeholder="Insira a cidade"
                                :disabled="!isEditMode"
                                v-bind="componentField" />
                        </FormControl>

                        <FormMessage />
                    </FormItem>
                </FormField>

                <FormField
                    v-slot="{ componentField }"
                    name="address.neighborhood"
                    :validate-on-blur="!isFieldDirty">
                    <FormItem>
                        <FormLabel>Bairro</FormLabel>
                        <FormControl>
                            <Input
                                type="text"
                                placeholder="Insira a cidade"
                                :disabled="!isEditMode"
                                v-bind="componentField" />
                        </FormControl>

                        <FormMessage />
                    </FormItem>
                </FormField>

                <FormField
                    v-slot="{ componentField }"
                    name="address.street"
                    :validate-on-blur="!isFieldDirty">
                    <FormItem>
                        <FormLabel>Logradouro</FormLabel>
                        <FormControl>
                            <Input
                                type="text"
                                placeholder="Insira o lagradouro"
                                :disabled="!isEditMode"
                                v-bind="componentField" />
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
                            <Input
                                type="text"
                                placeholder="Insira o número"
                                :disabled="!isEditMode"
                                v-bind="componentField" />
                        </FormControl>

                        <FormMessage />
                    </FormItem>
                </FormField>
            </div>

            <div class="flex flex-col gap-4">
                <div class="space-y-1">
                    <span class="text-xl font-medium">Contato</span>
                    <Separator />
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <FormField
                        v-slot="{ componentField }"
                        name="email"
                        :validate-on-blur="!isFieldDirty">
                        <FormItem>
                            <FormLabel>Email</FormLabel>
                            <FormControl>
                                <Input
                                    type="email"
                                    placeholder="Insira o email"
                                    :disabled="!isEditMode"
                                    v-bind="componentField" />
                            </FormControl>

                            <FormMessage />
                        </FormItem>
                    </FormField>
                    <FormField
                        v-slot="{ componentField }"
                        name="phone"
                        :validate-on-blur="!isFieldDirty">
                        <FormItem>
                            <FormLabel>Telefone</FormLabel>
                            <FormControl>
                                <Input
                                    id="phone"
                                    placeholder="Insara o número de telefone"
                                    v-maska="'(##) #####-####'"
                                    :disabled="!isEditMode"
                                    v-bind="componentField" />
                            </FormControl>

                            <FormMessage />
                        </FormItem>
                    </FormField>
                </div>
            </div>
        </CardContent>
    </Card>
</template>
