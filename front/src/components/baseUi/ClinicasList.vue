<template>
	<div class="overflow-hidden bg-white shadow-lg rounded-3xl">
		<div class="flex items-center justify-between p-4 text-white bg-primary">
			<h2 class="text-xl font-semibold">CLÍNICAS</h2>
			<button @click="navigateToAddClinic"
				class="px-4 py-2 text-blue-600 transition-colors bg-white rounded-md hover:bg-blue-100">
				Adicionar
			</button>
		</div>
		<ul>
			<li v-for="clinica in clinicas" :key="clinica.id" class="border-b last:border-b-0">
				<div class="flex items-center justify-between p-4 hover:bg-blue-200">
					<span>{{ clinica.name }}</span>
					<div class="max-lg:flex max-lg:flex-col max-lg:space-y-1">
						<button @click="editClinica(clinica.id)"
							class="px-3 py-1 mr-2 text-white transition-colors bg-blue-600 rounded-md hover:bg-blue-600 max-lg:w-full">
							Editar
						</button>
						<button @click="deleteClinica(clinica.id)"
							class="px-3 py-1 text-white transition-colors bg-red-500 rounded-md hover:bg-red-600">
							Desativar
						</button>
					</div>
				</div>
			</li>
		</ul>

		<dialog ref="modalDelete" id="exclusao" class="modal">
			<div class="modal-box">
				<h3 class="text-xl font-bold text-center">Tem certeza que deseja excluir?</h3>
				<div class="flex justify-center gap-4 mt-4">
					<button @click="closeModalDelete" class="text-black bg-gray-300 btn">
						Cancelar
					</button>
					<button @click="confirmActionDelete" class="text-white btn bg-primary">
						Confirmar
					</button>
				</div>
			</div>
			<form method="dialog" class="modal-backdrop">
				<button>Fechar</button>
			</form>
		</dialog>
	</div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import type { Clinic } from '@/types/clinica.types'
import { clinicService } from '@/services/clinic.service';


const clinicas = ref<Clinic[]>([])
onMounted( async () =>{
	try{
		const response = await clinicService.getAllClinics();
		console.log('Clinicas:',response)

		if(Array.isArray(response)){
			clinicas.value = response.map(clinica => ({
				...clinica,
				image:clinica.image?.startsWith('http')
				? clinica.image
				: `http://172.105.155.145${clinica.image.startsWith('/')?'' : '/'}${clinica.image}`
			}))
		} else {
			console.error("Formato de resposta inválido", response)
		}
	} catch(error){
		console.error('Erro ao buscar clinicas', error)
	}
})


// const props = defineProps<{
// 	clinicas: Clinic[]
// }>()

const router = useRouter()
const modalEdit = ref<HTMLDialogElement>()
const modalDelete = ref<HTMLDialogElement>()



//const clinicas = ref<Clinica[]>([
//	{ id: 1, name: 'Clínica Dr. Alexandre' },
//	{ id: 2, name: 'Clínica Maxado de Assis' },
//	{ id: 3, name: 'Clínica Odontológica Merci' },
//	{ id: 4, name: 'Clínica LolOdonto' },
//	{ id: 5, name: 'Clínica OdontoMed' },
//	{ id: 6, name: 'Clínica Sorriso' }
//])

const closeModalDelete = () => {
	modalDelete.value?.close()
}

const showModalDelete = () => {
	modalDelete.value?.showModal()
}

const navigateToAddClinic = () => {
	router.push('/dashboard/clinicas/cadastrar')
}

const editClinica = (id: number) => {
	console.log('Editar clinica')
}

const deleteClinica = (id: number) => {
	console.log('Delete clinica')
	showModalDelete()
}

const confirmActionDelete = () => {
	console.log('deleted')
}
</script>

<style scoped>
ul {
	list-style: none;
	padding: 0;
}

ul li:nth-child(even) {
	background-color: #deecfa;
}
</style>
