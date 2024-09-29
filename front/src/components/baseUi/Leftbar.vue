<template>
	<div class="flex flex-col w-[250px] px-4 py-8 items-center justify-between">
		<img class="w-32" src="../../assets/logo.svg" alt="" srcset="">

		<div class="flex flex-col mt-12 gap-y-1">
			<RouterLink class="router_link" v-for="item in navItems" :key="item.name" :to="item.path">
				<div class="flex items-center justify-start mt-4 mb-2 text-sm gap-x-4">
					<img :src="item.iconPath" alt="">
					<p class="text-lg font-bold">{{ item.name }}</p>
				</div>
			</RouterLink>
		</div>

		<!-- notificacoes -->
		<div class="flex flex-col mt-12 gap-y-1">
			<div class="flex flex-col p-4 bg-blue-200 shadow-lg rounded-2xl">
				<div class="self-end">
					<p class="text-xs">Seg 19:30</p>
				</div>
				<div class="flex items-start gap-x-2">
					<Bell fill="#054088" stroke="#054088" class="w-12" />
					<p class="text-sm">Solicitação aceita pelo paciente.</p>
				</div>
			</div>
		</div>


		<!-- ajuda (suporte, contatos, politicas) -->
		<div class="flex flex-col items-start w-full">
			<p class="font-bold">Ajuda</p>
			<RouterLink to="/suporte">Suporte</RouterLink>
			<RouterLink to="/contatos">Contatos</RouterLink>
			<RouterLink to="/politicas">Políticas</RouterLink>
		</div>

	</div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { Bell } from 'lucide-vue-next';

const route = useRoute();


//const isActive = (path: string) => computed(() => route.path === path);

const navItems = [
	{
		name: "Principal",
		iconPath: "src/assets/icons/principal.svg",
		path: "/dashboard",
		roles: ["admin", "superadmin", "medico", "recepcionista", "paciente"],
	},
	{
		name: "Institucional",
		iconPath: "src/assets/icons/institucional.svg",
		path: "/",
		roles: ["admin", "superadmin", "medico", "recepcionista", "paciente"],
	},
	{
		name: "Clinicas",
		iconPath: "src/assets/icons/clinicas.svg",
		path: "/dashboard/clinicas",
		roles: ["admin", "superadmin", "medico", "recepcionista", "paciente"],
	},
	{
		name: "Emails",
		iconPath: "src/assets/icons/email.svg",
		path: "/dashboard/emails",
		roles: ["admin", "superadmin", "medico", "recepcionista", "paciente"],
	}
];

</script>

<style scoped>
.slide-enter-active,
.slide-leave-active {
	transition: transform 0.3s ease;
}

.slide-enter-from,
.slide-leave-to {
	transform: translateX(-100%);
}

.leftbar-container.leftbar-closed .menu :where(li > details > summary):after,
.leftbar-container.leftbar-closed .menu :where(li > .menu-dropdown-toggle.menu-dropdown-show):after {
	display: none !important;
}

.menu :where(li:not(.menu-title) > *:not(ul, details, .menu-title, .btn)),
.menu :where(li:not(.menu-title) > details > summary:not(.menu-title)) {
	padding-left: 0.2rem;
	padding-right: 0.2rem;
}

.menu li>*:not(ul, .menu-title, details, .btn):active,
.menu li>*:not(ul, .menu-title, details, .btn).active,
.menu li>details>summary:active {
	background-color: unset;
	color: unset;
}

.sidebar-slide-fade-enter-active,
.sidebar-slide-fade-leave-active {
	transition:
		opacity 0.2s cubic-bezier(0.68, -0.55, 0.27, 1.55),
		transform 0.2s cubic-bezier(0.68, -0.55, 0.27, 1.55);
}

.sidebar-slide-fade-enter-from,
.sidebar-slide-fade-leave-to {
	opacity: 0;
	transform: translateX(20px);
}

.sidebar-slide-fade-leave-from,
.sidebar-slide-fade-enter-to {
	opacity: 1;
	transform: translateX(0);
}

.menu {
	padding: 0;
}

.menu :where(li:not(.menu-title) > *:not(ul, details, .menu-title, .btn)),
.menu :where(li:not(.menu-title) > details > summary:not(.menu-title)) {
	padding: 6px 8px;
}

.menu-link {
	color: #334155;
}

.active-link {
	/*background-color: #d6e3ff;*/
	font-weight: bold;
	border-left: 3px solid blue;
	border-radius: 0px;
	padding-left: 12px;
}

.link-transition {
	transition: all 0.1s ease-in-out;
}

.link-transition:focus {
	background-color: unset !important;
}

.active-link {
	background-color: #d6e3ff;
}

.router_link:hover {
	background-color: #f0f0f0;
}
</style>
