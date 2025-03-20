<template>
	<LayoutDashboard>
		<!-- Summary Cards -->
		<div class="flex gap-4 px-12 mt-12">
			<div class="p-4 bg-blue-100 rounded-lg shadow-lg min-w-56">
				<h3 class="text-3xl font-bold">{{ userStore.receptionists.length }}</h3>
				<p class="mt-2">Recepcionistas</p>
				<p class="font-bold">Hoje</p>
			</div>
			<div class="p-4 bg-yellow-100 rounded-lg shadow-lg min-w-56">
				<h3 class="text-3xl font-bold">3</h3>
				<p class="mt-2">Plantão hoje</p>
				<!-- Add small circular images here -->
			</div>
			<div class="p-4 bg-green-100 rounded-lg shadow-lg min-w-56">
				<h3 class="mb-8 text-xl font-bold">Cadastrar Recepcionistas</h3>
				<RouterLink to="/dashboard/recepcionista/cadastrar">
					<button class="py-2 w-full text-xs text-white btn bg-primary hover:bg-primary">
						Cadastrar
					</button>
				</RouterLink>
			</div>
			<div class="p-4 bg-white rounded-lg shadow-lg min-w-56">
				<h3 class="mb-8 text-xl font-bold">Pagamentos</h3>
				<button class="py-2 w-full text-xs text-white btn bg-primary hover:bg-primary">
					Acessar Asaas
				</button>
			</div>
		</div>

		<!-- Filter Tabs -->
		<div class="flex gap-x-4 items-center px-12 mt-8">
			<span class="font-bold">Recepcionistas</span>
			<button class="px-4 py-2 text-white bg-blue-700 rounded-full">Hoje</button>
			<select class="px-4 py-2 bg-gray-200 rounded-full">
				<option>Dias da semana</option>
				<option v-for="day in days_of_week" :key="day">{{ day }}</option>
				
			</select>
			<select class="px-4 py-2 bg-gray-200 rounded-full">
				<option>Turno</option>
				<option v-for="turn in turns" :key="turn">{{ turn }}</option>
			</select>
			
			<input type="text" v-model="searchName" class="px-4 py-2 bg-gray-200 rounded-full" placeholder="Pesquise..." />
			<button class="p-2 bg-gray-200 rounded-full">
				<Search />
			</button>
		</div>

		<!-- Receptionists Grid -->
		<div class="grid grid-cols-4 gap-4 px-12 mt-8">
			<div v-if="userStore.loading" class="col-span-4 text-center">Carregando recepcionistas...</div>
			<div v-else-if="userStore.error" class="col-span-4 text-center text-red-600">
				{{ userStore.error }}
			</div>
			<div v-else v-for="receptionist in filteredReceptionists" :key="receptionist.id"
				class="flex flex-col items-center p-4 bg-white rounded-lg shadow">
				<RouterLink :to="`/dashboard/recepcionistas/${receptionist.id}`">
					<img :src="`${apiAddress}${receptionist.attach_document}`" alt="Recepcionista"
						class="mx-auto w-24 h-24 rounded-full cursor-pointer" />
				</RouterLink>
				
				<h4 class="mt-2 font-bold text-center"> {{ receptionist.first_name }} </h4>
				<p class="text-sm text-center">Atendimento: 
					<p> <span>{{ formats(receptionist.expedient.days_of_week) }}</span> </p>
				</p>
				<p class="text-sm text-center">Turno: 
					<p> <span>{{ formats(receptionist.expedient.turns) }}</span> </p>
				</p>
				<div class="flex gap-x-2 mt-2">
					<Mail class="mx-auto w-6 h-6 text-blue-700" />
					<p class="text-sm text-center">{{ receptionist.email }}</p>
				</div>
				<div class="flex gap-x-2">
					<Phone class="mx-auto w-6 h-6 text-blue-700" />
					<p class="text-sm text-center">{{ receptionist.phone }}</p>
				</div>
			</div>
		</div>

		<!-- mensagem quando nao ha resultados -->
		<div v-if="!filteredReceptionists.length && !userStore.loading && !userStore.error"
			class="flex flex-col justify-center items-center mt-12 w-full">
			<img src="../../../assets/pacientes404.svg" alt="Recepcionistas" class="w-64" />
			<h2>Nenhum recepcionista encontrado</h2>
		</div>
	</LayoutDashboard>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { Search, Mail, Phone } from 'lucide-vue-next'
import { RouterLink } from 'vue-router'
import { useUserStore } from '@/stores/users/users.store'
import type { User } from '@/types/users.types'

const userStore = useUserStore()

// referencia para armazenar os recepcionistas
const receptionists = ref<User[]>([])
const apiAddress = 'http://191.252.192.82'

// referencias para os campos de busca
const searchName = ref('')
const searchEmail = ref('')
const days_of_week = ['Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo']
const turns = ['Matutino', 'Vespertino', 'Noturno']

// computed property para filtrar os recepcionistas
const filteredReceptionists = computed(() => {
	return receptionists.value.filter((receptionist) => {
		const fullName = `${receptionist.first_name} ${receptionist.last_name}`.toLowerCase()
		const matchName = fullName.includes(searchName.value.toLowerCase())
		const matchEmail = receptionist.email.toLowerCase().includes(searchEmail.value.toLowerCase())

		// retorna true se o nome ou email corresponderem à busca
		return (searchName.value === '' || matchName) && (searchEmail.value === '' || matchEmail)
	})
})

function formats(itens: String[]) {
	if (!itens || itens.length === 0) return ''; 
      if (itens.length === 1) return itens[0]; 

      
      const itensCopy = [...itens];
      const lastItem = itensCopy.pop(); 
      return itensCopy.join(', ') + ' e ' + lastItem; 
}

onMounted(async () => {
	try {
		await userStore.fetchReceptionists()
		receptionists.value = userStore.receptionists
	} catch (error) {
		console.error('erro ao carregar recepcionistas:', error)
	}
})
</script>
