<template>
	<LayoutDashboard>
		<div class="p-8">
			<h1 class="mb-6 text-4xl font-bold">{{ isEditMode ? 'Editar' : 'Cadastrar' }} Clínica</h1>

			<div class="p-6 mb-4 bg-white rounded-lg shadow-lg">
				<div class="flex gap-x-4 items-center mb-6">
					<label class="block mb-2 text-2xl font-semibold">Imagem da clínica:</label>
					<input type="file" accept="image/*" @change="handleImageUpload" class="hidden" ref="fileInput" />
					<button @click="triggerFileInput" class="px-2 py-2 text-white rounded bg-primary">
						Escolher arquivo
					</button>
					<span v-if="selectedImage" class="ml-2">{{ selectedImage.name }}</span>
				</div>

				<form @submit.prevent="submitForm">
					<h2 class="mb-4 text-xl font-semibold">Dados Principais:</h2>

					<div class="grid grid-cols-1 gap-4 md:grid-cols-2">
						<div>
							<label class="block mb-1">Nome da clínica:</label>
							<input v-model="formData.clinicName" type="text" class="px-2 py-1 w-full rounded border" />
						</div>
						<div>
							<label class="block mb-1">Nome do responsável:</label>
							<input v-model="formData.responsibleName" type="text"
								class="px-2 py-1 w-full rounded border" />
						</div>
						<div>
							<label class="block mb-1">RG do responsável:</label>
							<input v-model="formData.responsibleRG" type="text"
								class="px-2 py-1 w-full rounded border" />
						</div>
						<div>
							<label class="block mb-1">CPF do responsável:</label>
							<input v-model="formData.responsibleCPF" type="text"
								class="px-2 py-1 w-full rounded border" />
						</div>
						<div>
							<label class="block mb-1">CNPJ:</label>
							<input v-model="formData.cnpj" type="text" class="px-2 py-1 w-full rounded border" />
						</div>
					</div>

					<h2 class="mt-6 mb-4 text-xl font-semibold">Endereço:</h2>

					<div class="grid grid-cols-1 gap-4 md:grid-cols-2">
						<div>
							<label class="block mb-1">País:</label>
							<input v-model="formData.country" type="text" class="px-2 py-1 w-full rounded border" />
						</div>
						<div>
							<label class="block mb-1">Estado:</label>
							<input v-model="formData.state" type="text" class="px-2 py-1 w-full rounded border" />
						</div>
						<div>
							<label class="block mb-1">Cidade:</label>
							<input v-model="formData.city" type="text" class="px-2 py-1 w-full rounded border" />
						</div>
						<div>
							<label class="block mb-1">Bairro:</label>
							<input v-model="formData.neighborhood" type="text"
								class="px-2 py-1 w-full rounded border" />
						</div>
						<div>
							<label class="block mb-1">CEP:</label>
							<input v-model="formData.zipCode" type="text" class="px-2 py-1 w-full rounded border" />
						</div>
						<div>
							<label class="block mb-1">Logradouro:</label>
							<input v-model="formData.street" type="text" class="px-2 py-1 w-full rounded border" />
						</div>
						<div>
							<label class="block mb-1">Número:</label>
							<input v-model="formData.number" type="text" class="px-2 py-1 w-full rounded border" />
						</div>
					</div>

					<h2 class="mt-6 mb-4 text-xl font-semibold">Contato:</h2>

					<div class="grid grid-cols-1 gap-4 md:grid-cols-2">
						<div>
							<label class="block mb-1">Email:</label>
							<input v-model="formData.email" type="email" class="px-2 py-1 w-full rounded border" />
						</div>
						<div>
							<label class="block mb-1">Celular:</label>
							<input v-model="formData.phone" type="tel" class="px-2 py-1 w-full rounded border" />
						</div>
					</div>

					<div class="flex justify-end mt-8 space-x-4 max-lg:flex-col max-lg:space-y-4 max-lg:space-x-0">
						<button type="button" @click="saveAndAddAnother"
							class="px-4 py-2 text-white bg-blue-600 rounded">
							Salvar e adicionar outra(o)
						</button>
						<!-- <button
                            type="button"
                            @click="saveAndContinueEditing"
                            class="px-4 py-2 text-white bg-blue-600 rounded">
                            Salvar e continuar editando
                        </button> -->
						<button type="submit" class="px-4 py-2 text-white rounded bg-primary">
							Salvar
						</button>
					</div>
				</form>
			</div>
		</div>
	</LayoutDashboard>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { toast } from 'vue-sonner'
import { useClinicStore } from '@/stores/clinic/clinic.store'
import type { Clinic } from '@/types/clinic.types'
import { reject } from 'node_modules/cypress/types/bluebird'

const router = useRouter()
const route = useRoute()
const clinicStore = useClinicStore()
const fileInput = ref<HTMLInputElement | null>(null)
const selectedImage = ref<File | null>(null)
const isEditMode = ref(false)

// reactive pq formData é um objeto
const formData = reactive({
	clinicName: '',
	responsibleName: '',
	responsibleRG: '',
	responsibleCPF: '',
	cnpj: '',
	country: '',
	state: '',
	city: '',
	neighborhood: '',
	zipCode: '',
	street: '',
	number: '',
	email: '',
	phone: '',
	fileName:'',
	uploadedFile: null as File | null
})

onMounted(async () => {
	const clinicId = route.params.id as string
	if (clinicId) {
		isEditMode.value = true
		try {
			await clinicStore.fetchSingleClinic(clinicId)
			if (clinicStore.currentClinic) {
				formData.clinicName = clinicStore.currentClinic.name
				formData.responsibleName = clinicStore.currentClinic.nome_responsavel
				formData.responsibleRG = clinicStore.currentClinic.rg_responsavel
				formData.responsibleCPF = clinicStore.currentClinic.cpf_responsavel
				formData.cnpj = clinicStore.currentClinic.cnpj
				formData.email = clinicStore.currentClinic.email_responsavel
				formData.phone = clinicStore.currentClinic.telefone_responsavel

				if (clinicStore.currentClinic.address) {
					formData.country = clinicStore.currentClinic.address.country
					formData.state = clinicStore.currentClinic.address.state
					formData.city = clinicStore.currentClinic.address.city
					formData.neighborhood = clinicStore.currentClinic.address.neighborhood
					formData.zipCode = clinicStore.currentClinic.address.zip_code
					formData.street = clinicStore.currentClinic.address.street
					formData.number = clinicStore.currentClinic.address.number
				}
			}
		} catch (error) {
			toast.error('Erro ao carregar dados da clínica')
			console.error('Error fetching clinic:', error)
		}
	}
})

const handleImageUpload = (event: Event) => {
	const target = event.target as HTMLInputElement
	if (target.files && target.files.length > 0) {
		selectedImage.value = target.files[0]
	}
}

// formata os dados da clínica para o formato esperado pelo backend
const formatClinicData = async (): Promise<Clinic> => {
	let base64Image = ''

	if (selectedImage.value) {
		base64Image = await convertImageToBase64(selectedImage.value)
	}

	return {
		name: formData.clinicName,
		nome_responsavel: formData.responsibleName,
		cnpj: formData.cnpj,
		rg_responsavel: formData.responsibleRG,
		telefone_responsavel: formData.phone,
		cpf_responsavel: formData.responsibleCPF,
		email_responsavel: formData.email,
		image: base64Image || (clinicStore.currentClinic?.image || ''),
		address: {
			country: formData.country,
			state: formData.state,
			city: formData.city,
			neighborhood: formData.neighborhood,
			zip_code: formData.zipCode,
			street: formData.street,
			number: formData.number
		}
	}
}

const convertImageToBase64 = (file: File): Promise<string> => {
	return new Promise((resolve, reject) =>{
		const reader = new FileReader()

		reader.onload = () =>{
			const result = reader.result as string
			resolve(result.split(',')[1]) // Para remover o prefixo 'data:image/png;base64,'
		}

		reader.onerror = (error) => (error)

		reader.readAsDataURL(file)
	})
}

const triggerFileInput = () => {
	fileInput.value?.click()
}

const formatErrorMessage = (error: any): string => {
	if (error?.errors) {
		const messages = Object.entries(error.errors)
			.map(([field, messages]) => {
				const fieldTranslations: { [key: string]: string } = {
					'image': 'Imagem',
					'name': 'Nome',
					'cnpj': 'CNPJ',
					'rg_responsavel': 'RG do responsável',
					'cpf_responsavel': 'CPF do responsável',
					'email_responsavel': 'Email do responsável',
					'telefone_responsavel': 'Telefone do responsável'
				}
				const translatedField = fieldTranslations[field] || field
				return `${translatedField}: ${(messages as string[]).join(', ')}`
			})
		return messages.join('\n')
	}
	return error?.message || 'Erro ao cadastrar clínica'
}

const submitForm = async () => {
	try {
		const clinicData = await formatClinicData()
		console.log('clinicData:', clinicData)
		
		let result;


		if (isEditMode.value) {
			const clinicId = Number(route.params.id)
			result = await clinicStore.updateClinic(clinicId, clinicData)
			if (result) {
				toast.success('Clínica atualizada com sucesso!')
			}
		} else {
			result = await clinicStore.createClinic(clinicData)
			if (result) {
				toast.success('Clínica cadastrada com sucesso!')
			}
		}

		if (!result) {
			toast.error(`Erro ao ${isEditMode.value ? 'atualizar' : 'cadastrar'} clínica. Por favor, tente novamente.`)
			return
		}

		router.push('/dashboard/clinicas')
	} catch (error: any) {
		const errorMessage = formatErrorMessage(error)
		toast.error(errorMessage)
		console.error(`Erro ao ${isEditMode.value ? 'atualizar' : 'cadastrar'} clínica:`, error)
	}
}

const saveAndAddAnother = async () => {
	if (isEditMode.value) {
		toast.error('Esta opção não está disponível no modo de edição')
		return
	}

	try {
		const clinicData = await formatClinicData()
		const result = await clinicStore.createClinic(clinicData)

		if (!result) {
			toast.error('Erro ao cadastrar clínica. Por favor, tente novamente.')
			return
		}

		toast.success('Clínica cadastrada com sucesso!')
		// Reset form data
		Object.keys(formData).forEach((key) => {
			formData[key as keyof typeof formData] = ''
		})
		selectedImage.value = null
	} catch (error: any) {
		const errorMessage = formatErrorMessage(error)
		toast.error(errorMessage)
		console.error('Erro ao cadastrar clínica:', error)
	}
}

// const saveAndContinueEditing = async () => {
//     try {
//         const clinicData = formatClinicData()
//         const newClinic = await clinicStore.createClinic(clinicData)
//         toast.success('Clínica cadastrada com sucesso!')
//         router.push(`/dashboard/clinicas/editar/${newClinic.uuid}`)
//     } catch (error) {
//         toast.error('Erro ao cadastrar clínica')
//         console.error(error)
//     }
// }

</script>