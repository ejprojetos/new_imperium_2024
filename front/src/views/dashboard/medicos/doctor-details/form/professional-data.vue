<script setup lang="ts">
import { ref, computed } from 'vue'
import { FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form'
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Separator } from '@/components/ui/separator'
import { ChevronsUpDown, Upload, Check } from 'lucide-vue-next'
import { cn } from '@/lib/utils'
import { Loader } from 'lucide-vue-next'
import {
    Combobox,
    ComboboxAnchor,
    ComboboxEmpty,
    ComboboxGroup,
    ComboboxInput,
    ComboboxItem,
    ComboboxItemIndicator,
    ComboboxList,
    ComboboxTrigger
} from '@/components/ui/combobox'
import { academicFormations, medicalSpecialties } from '../data'
import {
    Select,
    SelectContent,
    SelectGroup,
    SelectItem,
    SelectTrigger,
    SelectValue
} from '@/components/ui/select'
import { vMaska } from 'maska/vue'
import { Button } from '@/components/ui/button'

const props = defineProps<{
    isEditMode: boolean
    isFieldDirty: any
    imageUrl: string | null
    onRemoveFile: () => void
}>()

const selectedImageUrl = ref<string | null>(props.imageUrl)

const handleFileChange = (event: Event) => {
    const fileInput = event.target as HTMLInputElement
    if (fileInput.files && fileInput.files[0]) {
        const file = fileInput.files[0]

        selectedImageUrl.value = URL.createObjectURL(file)
    }
}

const displayImage = computed(() => selectedImageUrl.value || props.imageUrl)

function handleRemoveImg() {
    props.onRemoveFile()
    selectedImageUrl.value = null
}
</script>

<template>
    <Card>
        <CardHeader>
            <CardTitle>Dados Profissionais</CardTitle>
            <CardDescription>
                Essas informações são essenciais para validar e registrar o profissional
                corretamente.
            </CardDescription>
            <span
                v-if="isEditMode"
                class="absolute right-8 bg-yellow-300/40 border border-yellow-700 rounded-full px-2 py-0.5 font-medium text-sm">
                Modo edição
            </span>
        </CardHeader>
        <CardContent class="grid grid-cols-2 gap-4 items-end">
            <FormField v-slot="{ componentField }" name="formation">
                <FormItem>
                    <FormLabel>Formação</FormLabel>

                    <Select v-bind="componentField">
                        <FormControl>
                            <SelectTrigger class="w-full" :disabled="!isEditMode">
                                <SelectValue placeholder="Select a option" />
                            </SelectTrigger>
                        </FormControl>
                        <SelectContent>
                            <SelectGroup>
                                <SelectItem
                                    v-for="formation in academicFormations"
                                    :key="formation.id"
                                    :value="formation.id">
                                    {{ formation.label }}
                                </SelectItem>
                            </SelectGroup>
                        </SelectContent>
                    </Select>

                    <FormMessage />
                </FormItem>
            </FormField>
            <FormField name="specialty">
                <FormItem class="flex flex-col">
                    <FormLabel>Especialidade</FormLabel>

                    <Combobox by="label">
                        <FormControl>
                            <ComboboxAnchor>
                                <div class="relative">
                                    <ComboboxInput
                                        :display-value="(val) => val?.label ?? ''"
                                        placeholder="Selecione uma especialidade..." />
                                    <ComboboxTrigger
                                        class="absolute end-0 inset-y-0 flex items-center justify-center px-3">
                                        <ChevronsUpDown class="size-4 text-muted-foreground" />
                                    </ComboboxTrigger>
                                </div>
                            </ComboboxAnchor>
                        </FormControl>

                        <ComboboxList align="start" class="max-h-80">
                            <ComboboxEmpty>Nothing found.</ComboboxEmpty>

                            <ComboboxGroup>
                                <ComboboxItem
                                    v-for="specility in medicalSpecialties"
                                    :key="specility.id"
                                    :value="specility">
                                    {{ specility.label }}

                                    <ComboboxItemIndicator>
                                        <Check :class="cn('ml-auto h-4 w-4')" />
                                    </ComboboxItemIndicator>
                                </ComboboxItem>
                            </ComboboxGroup>
                        </ComboboxList>
                    </Combobox>

                    <FormMessage />
                </FormItem>
            </FormField>
            <div class="col-span-1">
                <FormField v-slot="{ componentField }" name="crm" :validate-on-blur="!isFieldDirty">
                    <FormItem>
                        <FormLabel>CRM</FormLabel>
                        <FormControl>
                            <Input
                                type="text"
                                placeholder="UF-123456 ou UF-123456/7"
                                v-maska="'@@-######/##'"
                                maxlength="11"
                                :disabled="!isEditMode"
                                v-bind="componentField" />
                        </FormControl>

                        <FormMessage />
                    </FormItem>
                </FormField>
            </div>

            <Separator class="col-span-2" />

            <div class="col-span-2">
                <FormField
                    v-slot="{ componentField }"
                    name="file"
                    :validate-on-blur="!isFieldDirty">
                    <FormItem>
                        <div class="flex gap-4">
                            <div
                                v-if="displayImage"
                                class="h-40 max-w-48 rounded-md border p-2 flex items-center justify-center">
                                <img v-if="displayImage" :src="displayImage" class="h-40" />
                                <Loader
                                    v-if="displayImage === undefined"
                                    class="animate-spin size-4 text-gray-300" />
                            </div>

                            <FormControl class="flex flex-col">
                                <div class="flex">
                                    <FormLabel class="mb-4">Documento comprobatório</FormLabel>

                                    <FormLabel
                                        :class="[
                                            'relative cursor-pointer h-9 w-[160px] px-3 py-2 inline-flex items-center bg-gray-200 gap-2 justify-center rounded-lg text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
                                            !isEditMode && 'opacity-50 pointer-events-none'
                                        ]">
                                        <Upload class="size-4" />
                                        <span class="text-sm">Inserir arquivo...</span>
                                        <input
                                            type="file"
                                            class="border opacity-0 absolute inset-0 w-full h-full cursor-pointer"
                                            placeholder="Insirir documento"
                                            :disabled="!isEditMode"
                                            v-bind="componentField"
                                            @change="handleFileChange" />
                                    </FormLabel>
                                    <div class="text-xs text-gray-500 my-2">
                                        O Tamanho máximo do arquivo é de 5MB (PNG, JPG, JPEG)
                                    </div>
                                    <Button
                                        type="button"
                                        v-if="displayImage"
                                        :disabled="!isEditMode && displayImage"
                                        size="sm"
                                        variant="destructive"
                                        class="w-[160px]"
                                        @click="handleRemoveImg">
                                        Remover
                                    </Button>
                                </div>
                            </FormControl>

                            <FormMessage />
                        </div>
                    </FormItem>
                </FormField>
            </div>
        </CardContent>
    </Card>
</template>
