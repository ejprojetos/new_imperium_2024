<template>
	<div class="flex flex-col  w-[250px] px-4 py-8 items-center">
		<img class="w-32 " src="../../assets/logo.svg" alt="" srcset="">
	</div>
</template>

<script setup lang="ts">
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
</style>
