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

const selectedFile = ref<File | null>(null)
const selectedImageUrl = ref<string | null>(null)

const handleFileChange = (event: Event) => {
    const fileInput = event.target as HTMLInputElement
    if (fileInput.files && fileInput.files[0]) {
        const file = fileInput.files[0]
        selectedFile.value = file

        if (file.type.startsWith('image/')) {
            selectedImageUrl.value = URL.createObjectURL(file)
        } else {
            selectedImageUrl.value = null // no preview for non-image files
        }
    }
}

const displayAsPdf = computed(() => {
    return selectedFile.value?.type === 'application/pdf'
})

function handleRemoveImg() {
    props.onResetDocumentImg()
    selectedImageUrl.value = null
    selectedFile.value = null
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
                    <Transition name="fade-zoom">
                        <div
                            v-if="selectedImageUrl || displayAsPdf"
                            class="h-40 w-full max-w-48 rounded-md border p-2 flex items-center justify-center">
                            <img
                                v-if="selectedImageUrl"
                                :src="selectedImageUrl"
                                class="h-36 m-auto object-contain" />
                            <div
                                v-else-if="displayAsPdf"
                                class="text-center flex flex-col items-center">
                                <svg viewBox="0 0 309.267 309.267" xml:space="preserve">
                                    <g>
                                        <path
                                            style="fill: #e2574c"
                                            d="M38.658,0h164.23l87.049,86.711v203.227c0,10.679-8.659,19.329-19.329,19.329H38.658 c-10.67,0-19.329-8.65-19.329-19.329V19.329C19.329,8.65,27.989,0,38.658,0z" />
                                        <path
                                            style="fill: #b53629"
                                            d="M289.658,86.981h-67.372c-10.67,0-19.329-8.659-19.329-19.329V0.193L289.658,86.981z" />
                                        <path
                                            style="fill: #ffffff"
                                            d="M217.434,146.544c3.238,0,4.823-2.822,4.823-5.557c0-2.832-1.653-5.567-4.823-5.567h-18.44
		c-3.605,0-5.615,2.986-5.615,6.282v45.317c0,4.04,2.3,6.282,5.412,6.282c3.093,0,5.403-2.242,5.403-6.282v-12.438h11.153
		c3.46,0,5.19-2.832,5.19-5.644c0-2.754-1.73-5.49-5.19-5.49h-11.153v-16.903C204.194,146.544,217.434,146.544,217.434,146.544z
		 M155.107,135.42h-13.492c-3.663,0-6.263,2.513-6.263,6.243v45.395c0,4.629,3.74,6.079,6.417,6.079h14.159
		c16.758,0,27.824-11.027,27.824-28.047C183.743,147.095,173.325,135.42,155.107,135.42z M155.755,181.946h-8.225v-35.334h7.413
		c11.221,0,16.101,7.529,16.101,17.918C171.044,174.253,166.25,181.946,155.755,181.946z M106.33,135.42H92.964
		c-3.779,0-5.886,2.493-5.886,6.282v45.317c0,4.04,2.416,6.282,5.663,6.282s5.663-2.242,5.663-6.282v-13.231h8.379
		c10.341,0,18.875-7.326,18.875-19.107C125.659,143.152,117.425,135.42,106.33,135.42z M106.108,163.158h-7.703v-17.097h7.703
		c4.755,0,7.78,3.711,7.78,8.553C113.878,159.447,110.863,163.158,106.108,163.158z" />
                                    </g>
                                </svg>
                                <span class="text-sm mt-2 text-gray-600">Arquivo PDF</span>
                            </div>
                        </div>
                    </Transition>

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
                                O Tamanho máximo do arquivo é de 5MB (PNG, JPG, JPEG ou PDF)
                            </div>
                            <Button
                                type="button"
                                v-if="selectedImageUrl || displayAsPdf"
                                :disabled="!(selectedImageUrl || displayAsPdf)"
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

<style scoped>
.fade-zoom-enter-active,
.fade-zoom-leave-active {
    transition: all 0s ease;
}
.fade-zoom-enter-from,
.fade-zoom-leave-to {
    opacity: 0;
    transform: scale(0.95);
}
.fade-zoom-enter-to,
.fade-zoom-leave-from {
    opacity: 1;
    transform: scale(1);
}
</style>
