<template>
	<LayoutDashboard>
		<div class="p-8">
			<h1 class="mb-6 text-4xl font-bold">Clínicas</h1>
			<ClinicasList :clinics="clinics" />
		</div>
	</LayoutDashboard>
</template>

<script setup lang="ts">
import ClinicasList from '@/components/baseUi/ClinicasList.vue';
import LayoutDashboard from '@/layouts/LayoutDashboard.vue';
import { useClinicStore } from '@/stores/clinic/clinic.store'
import { storeToRefs } from 'pinia';
import { ref, onMounted } from 'vue';

const clinicStore = useClinicStore()
const { clinics } = storeToRefs(clinicStore)


onMounted(async () => {
	await clinicStore.fetchClinics()
})


</script>
