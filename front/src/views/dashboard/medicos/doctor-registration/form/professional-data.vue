<script setup lang="ts">
import { ref, computed } from 'vue'
import { FormField, FormItem, FormLabel, FormControl, FormMessage } from '@/components/ui/form'
import { Input } from '@/components/ui/input'
import { Separator } from '@/components/ui/separator'
import { vMaska } from 'maska/vue'
import { academicFormations } from '@/utils/data'
import {
    Select,
    SelectTrigger,
    SelectContent,
    SelectGroup,
    SelectItem,
    SelectValue
} from '@/components/ui/select'
import { Upload } from 'lucide-vue-next'
import { Button } from '@/components/ui/button'

const props = defineProps<{
    isFieldDirty: any
    onResetDocumentImg(): void
}>()

const selectedImageUrl = ref<string | null>(null)

const handleFileChange = (event: Event) => {
    const fileInput = event.target as HTMLInputElement
    if (fileInput.files && fileInput.files[0]) {
        const file = fileInput.files[0]

        selectedImageUrl.value = URL.createObjectURL(file)
    }
}

const displayImage = computed(() => selectedImageUrl.value)

function handleRemoveImg() {
    props.onResetDocumentImg()
    selectedImageUrl.value = null
}
</script>

<template>
    <div class="grid grid-cols-2 gap-4">
        <div class="space-y-1 col-span-2">
            <span class="text-xl font-medium">Dados Profissionais</span>
            <Separator />
        </div>

        <FormField v-slot="{ componentField }" name="formation">
            <FormItem class="col-span-2 md:col-span-1">
                <FormLabel>Formação</FormLabel>

                <Select v-bind="componentField">
                    <FormControl>
                        <SelectTrigger class="w-full">
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

        <FormField v-slot="{ componentField }" name="crm" :validate-on-blur="!isFieldDirty">
            <FormItem class="col-span-2 md:col-span-1">
                <FormLabel>CRM</FormLabel>
                <FormControl>
                    <Input
                        type="text"
                        placeholder="UF-123456 ou UF-123456/7"
                        v-maska="'@@-######/##'"
                        maxlength="11"
                        v-bind="componentField" />
                </FormControl>

                <FormMessage />
            </FormItem>
        </FormField>

        <FormField v-slot="{ componentField }" name="file" :validate-on-blur="!isFieldDirty">
            <FormItem class="col-span-2 mt-6 mb-4">
                <div class="flex gap-4">
                    <div
                        v-if="displayImage"
                        class="h-40 w-full max-w-48 rounded-md border p-2 flex items-center justify-center">
                        <img v-if="displayImage" :src="displayImage" class="h-40 m-auto" />
                        <Loader v-if="displayImage" class="animate-spin size-4 text-gray-600" />
                    </div>

                    <FormControl class="flex flex-col">
                        <div class="flex">
                            <FormLabel class="mb-4">Documento comprobatório</FormLabel>

                            <FormLabel
                                :class="[
                                    'relative cursor-pointer h-9 w-[160px] px-3 py-2 inline-flex items-center bg-gray-200 gap-2 justify-center rounded-lg text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50'
                                ]">
                                <Upload class="size-4" />
                                <span class="text-sm">Inserir arquivo...</span>
                                <input
                                    type="file"
                                    class="border opacity-0 absolute inset-0 w-full h-full cursor-pointer"
                                    placeholder="Insirir documento"
                                    v-bind="componentField"
                                    @change="handleFileChange" />
                            </FormLabel>
                            <div class="text-xs text-gray-500 my-2">
                                O Tamanho máximo do arquivo é de 5MB (PNG, JPG, JPEG)
                            </div>
                            <Button
                                type="button"
                                v-if="displayImage"
                                :disabled="!displayImage"
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
</template>
