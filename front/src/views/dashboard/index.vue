<template>
	<LayoutDashboard>
		<div
			class="flex items-center justify-between w-full px-12 mt-12 max-lg:flex-col max-lg:items-start max-lg:px-2">
			<h1 class="text-5xl font-bold">Minhas Clínicas</h1>

			<!--Cards-->
			<div
				class="flex gap-x-4 max-lg:flex-col max-lg:items-start max-lg:gap-x-0 max-lg:w-full max-lg:gap-y-4 max-lg:mt-4">
				<div class="p-4 rounded-lg shadow-lg bg-lightGreen min-w-56 max-lg:w-full">
					<h3 class="mb-8 text-xl font-bold">Cadastrar clínica</h3>
					<RouterLink to="/dashboard/clinicas/cadastrar">
						<button class="w-full py-2 text-xs text-white min-h-unset btn bg-primary hover:bg-primary">
							Cadastrar
						</button>
					</RouterLink>
				</div>
				<div class="p-4 bg-white rounded-lg shadow-lg min-w-56 max-lg:w-full">
					<h3 class="mb-8 text-xl font-bold">Pagamentos</h3>
					<button class="w-full py-2 text-xs text-white min-h-unset btn bg-primary hover:bg-primary">
						Cadastrar
					</button>
				</div>
			</div>
		</div>

		<!-- search -->

		<div
			class="flex items-center justify-between px-12 py-2 mx-12 mt-12 rounded-full max-lg:px-2 max-lg:mx-0 bg-lightBlue">
			<p>Clínicas</p>

			<div class="flex items-center gap-x-4">
				<div class="px-6 py-2 text-xs text-white rounded-full bg-primary">Todas</div>

				<select
					class="w-full max-w-xs rounded-full select select-bordered select-sm border-primary bg-lightBlue">
					<option disabled selected>Cidade</option>
				</select>

				<select
					class="w-full max-w-xs rounded-full select select-bordered select-sm border-primary bg-lightBlue">
					<option disabled selected>Bairro</option>
				</select>
				<input type="text" placeholder="CPF"
					class="w-full max-w-xs rounded-full input input-bordered input-sm border-primary bg-lightBlue custom-placeholder" />
				<input type="text" placeholder="Nome"
					class="w-64 rounded-full w- input input-bordered input-sm border-primary bg-lightBlue custom-placeholder" />

				<Search class="w-32 cursor-pointer" />
			</div>
		</div>

		<!-- grid 2 columns and on mobile 1 column -->
		<div class="grid grid-cols-1 gap-4 px-12 mt-12 max-lg:px-2 md:grid-cols-2">
			<!--Cards-->
			<div v-for="clinica in clinicas" :key="clinica.name"
				class="flex p-8 bg-white shadow-lg cursor-pointer rounded-2xl min-w-56 gap-x-6">
				<img class="object-cover w-24 h-24 rounded-full aspect-square"
					:src="clinica.image || '../../../src/assets/placeholder.png'" alt="Imagem da clínica" />
				<div class="flex flex-col items-start">
					<h3 class="text-2xl font-bold">{{ clinica.name }}</h3>
					<p class="text-lg">{{ clinica.address.street }}</p>
				</div>
			</div>
			<!-- <div
                v-for="card in cards"
                :key="card.title"
                class="flex p-8 bg-white shadow-lg cursor-pointer rounded-2xl min-w-56 gap-x-6">
                <img class="aspect-square" src="../../../src/assets/placeholder.png" alt="" />
                <div class="flex flex-col items-start">
                    <h3 class="text-2xl font-bold">{{ card.title }}</h3>
                    <p class="text-lg">{{ card.street }}</p>
                </div>
            </div> -->
		</div>
	</LayoutDashboard>
</template>

<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { Search } from 'lucide-vue-next'
import { RouterLink } from 'vue-router'
import { ref, onMounted } from 'vue'
import type { Clinic } from '@/types/clinic.types'
import { clinicService } from '@/services/clinic.service'


const clinicas = ref<Clinic[]>([])

onMounted(async () => {
	try {
		const response = await clinicService.getAllClinics();
		console.log('Clinicas: ', response)
		clinicas.value = response
		//if(Array.isArray(response)){
		//    clinicas.value = response.map(clinica =>({
		//        ...clinica,
		//        image:clinica.image?.startsWith('http')
		//        ? clinica.image
		//        :`http://172.105.155.145${clinica.image.startsWith('/')?'' : '/'}${clinica.image}`
		//    }))
		//}else{
		//    console.error('Formato de resposta invalido', response)
		//}
	} catch (error) {
		console.error('Erro ao buscar clinicas', error)
	}
})

const cards = [
	{
		img: 'https://picsum.photos/id/10/400/200',
		title: 'Clínica Dr. Alexandre',
		street: 'Rua Amâncio Campos 117, RN – 59002-970',
		button: 'Cadastrar',
		link: '/dashboard/clinics/1'
	},
	{
		img: 'https://picsum.photos/id/20/400/200',
		title: 'Clínica Maxado de Assis',
		street: 'Rua Balduíno Guedes 95, RN – 59355-970',
		button: 'Cadastrar',
		link: '/dashboard/clinics/2'
	},
	{
		img: 'https://picsum.photos/id/30/400/200',
		title: 'Clínica Odontologica Merci',
		street: 'Rua Principal 557, RN – 59390-972',
		button: 'Cadastrar',
		link: '/dashboard/clinics/3'
	},
	{
		img: 'https://picsum.photos/id/40/400/200',
		title: 'Clínica LoiOdonto',
		street: 'Rua Jardim Acácia 101, RN – 59114-700',
		button: 'Cadastrar',
		link: '/dashboard/clinics/4'
	},
	{
		img: 'https://picsum.photos/id/50/400/200',
		title: 'Clínica OdontoMed',
		street: 'Rua André Martins da Silva 09, RN – 59157-160',
		button: 'Cadastrar',
		link: '/dashboard/clinics/5'
	},
	{
		img: 'https://picsum.photos/id/60/400/200',
		title: 'Clínica Sorriso',
		street: 'Rua Parque Iiporã 34, RN – 59144-136',
		button: 'Cadastrar',
		link: '/dashboard/clinics/6'
	}
]
</script>

<style scoped>
.min-h-unset {
	min-height: unset;
	height: unset;
}

.custom-placeholder::placeholder {
	color: #121212;
}
</style>
