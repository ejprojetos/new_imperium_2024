<template>
	<!-- Desktop -->
	<div v-if="!isMobile" class="flex items-center justify-end h-12 px-4 bg-white ">
		<p class="font-bold">Olá, {{ role }}</p>
	</div>

	<!-- Mobile -->
	<div v-else class="flex items-center justify-between h-12 px-4 bg-white border-b border-gray-200">
		topbar mobile
	</div>
</template>

<script setup>
import { storeToRefs } from "pinia";
import { ref } from "vue";
import { useScreenSize } from "@/composables/useScreenSize";

const { isMobile } = useScreenSize();

//const { user } = storeToRefs(useUserStore());
const role = ref("Administrador");

</script>
