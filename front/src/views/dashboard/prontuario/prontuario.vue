<template>
    <LayoutDashboard>
        <div class="p-8">
            <div class="flex items-center mb-6 w-full max-w-[1000px] mx-auto">
                <RouterLink
                    to="/dashboard"
                    class="flex items-center text-blue-600 hover:text-blue-800 mb-4">
                    <span class="mr-2">←</span>
                    <span>Voltar</span>
                </RouterLink>
            </div>

            <div class="p-6 bg-white rounded-lg shadow-lg max-w-[1000px] mx-auto">
                <h1 class="text-2xl font-bold mb-6">Prontuário</h1>

                <div class="grid grid-cols-2 gap-4 mb-6">
                    <div>
                        <label class="block mb-1 font-semibold">Data da consulta:</label>
                        <p v-if="!isEditing">{{ formData.consultDate }}</p>
                        <input
                            v-else
                            v-model="formData.consultDate"
                            type="date"
                            class="w-full px-2 py-1 border rounded" />
                    </div>
                    <div>
                        <label class="block mb-1 font-semibold">Horário da consulta:</label>
                        <p v-if="!isEditing">{{ formData.consultTime }}</p>
                        <input
                            v-else
                            v-model="formData.consultTime"
                            type="time"
                            class="w-full px-2 py-1 border rounded" />
                    </div>
                </div>

                <div class="mb-6">
                    <label class="block mb-1 font-semibold">Médico responsável:</label>
                    <div class="flex items-center">
                        <img
                            :src="formData.doctorImage"
                            alt="Doctor"
                            class="w-8 h-8 rounded-full mr-2" />
                        <span>{{ formData.doctorName }}</span>
                    </div>
                </div>

                <div class="mb-6">
                    <label class="block mb-1 font-semibold">Local:</label>
                    <p>{{ formData.location }}</p>
                </div>

                <div class="mb-6">
                    <label class="block mb-1 font-semibold">Nome do paciente:</label>
                    <p>{{ formData.patientName }}</p>
                </div>

                <div class="space-y-6">
                    <div>
                        <label class="block mb-1 font-semibold">Alergias:</label>
                        <p v-if="!isEditing">{{ formData.allergies }}</p>
                        <textarea
                            v-else
                            v-model="formData.allergies"
                            rows="3"
                            class="w-full px-2 py-1 border rounded"
                            placeholder="Alergias do paciente"></textarea>
                    </div>

                    <div>
                        <label class="block mb-1 font-semibold">Problemas recorrentes:</label>
                        <p v-if="!isEditing">{{ formData.recurringProblems }}</p>
                        <textarea
                            v-else
                            v-model="formData.recurringProblems"
                            rows="3"
                            class="w-full px-2 py-1 border rounded"
                            placeholder="Doenças/sintomas que o paciente possui antes da consulta"></textarea>
                    </div>

                    <div>
                        <label class="block mb-1 font-semibold">Medicação:</label>
                        <p v-if="!isEditing">{{ formData.medication }}</p>
                        <textarea
                            v-else
                            v-model="formData.medication"
                            rows="3"
                            class="w-full px-2 py-1 border rounded"
                            placeholder="Remédios que o paciente já toma antes da consulta ou que foi prescrito em consultas anteriores"></textarea>
                    </div>

                    <div>
                        <label class="block mb-1 font-semibold">Anamnese:</label>
                        <p v-if="!isEditing">{{ formData.anamnesis }}</p>
                        <textarea
                            v-else
                            v-model="formData.anamnesis"
                            rows="3"
                            class="w-full px-2 py-1 border rounded"
                            placeholder="Breve entrevista com o paciente. 1º diagnóstico"></textarea>
                    </div>

                    <div>
                        <label class="block mb-1 font-semibold">Nova medicação:</label>
                        <p v-if="!isEditing">{{ formData.newMedication }}</p>
                        <textarea
                            v-else
                            v-model="formData.newMedication"
                            rows="3"
                            class="w-full px-2 py-1 border rounded"
                            placeholder="Prescrição dos remédios após a consulta"></textarea>
                    </div>

                    <div>
                        <label class="block mb-1 font-semibold">Exames:</label>
                        <p v-if="!isEditing">{{ formData.exams }}</p>
                        <textarea
                            v-else
                            v-model="formData.exams"
                            rows="3"
                            class="w-full px-2 py-1 border rounded"
                            placeholder="Necessidade de exames médicos"></textarea>
                    </div>
                </div>

                <div class="flex justify-end mt-8">
                    <button
                        v-if="!isEditing"
                        @click="startEditing"
                        class="px-4 py-2 text-white bg-blue-600 rounded">
                        Editar
                    </button>
                    <template v-else>
                        <button
                            @click="cancelEditing"
                            class="px-4 py-2 mr-2 text-gray-700 bg-gray-200 rounded">
                            Cancelar
                        </button>
                        <button
                            @click="saveChanges"
                            class="px-4 py-2 text-white bg-blue-600 rounded">
                            Salvar
                        </button>
                    </template>
                </div>
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { RouterLink } from 'vue-router'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'

interface ProntuarioData {
    consultDate: string
    consultTime: string
    doctorImage: string
    doctorName: string
    location: string
    patientName: string
    allergies: string
    recurringProblems: string
    medication: string
    anamnesis: string
    newMedication: string
    exams: string
}

const isEditing = ref(false)
const originalData = ref<ProntuarioData | null>(null)

const formData = reactive<ProntuarioData>({
    consultDate: '29/02/2019',
    consultTime: '12:00',
    doctorImage: '../../../assets/placeholder.png',
    doctorName: 'Dra. Rafaela Veríssimo',
    location: 'Sala 02',
    patientName: 'Gabriele Rocha de Carvalho',
    allergies: '',
    recurringProblems: '',
    medication: '',
    anamnesis: '',
    newMedication: '',
    exams: ''
})

function startEditing() {
    originalData.value = JSON.parse(JSON.stringify(formData))
    isEditing.value = true
}

function cancelEditing() {
    if (originalData.value) {
        Object.assign(formData, originalData.value)
    }
    isEditing.value = false
}

function saveChanges() {
    console.log('Saving changes:', formData)
    isEditing.value = false
}
</script>
