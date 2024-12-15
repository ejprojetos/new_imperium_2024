<template>
	<NavBarHome />
	<section class="secao-login">
		<div class="secao-texto">
			<h1 class="texto-bem-vindos"> BEM VINDOS</h1>
		</div>
		<div>
			<div class="secao-bem-vindos primeira-div">

			</div>
			<div class="secao-bem-vindos segunda-div">

			</div>
		</div>

		<div class="p-6 rounded-lg shadow-lg max-w-[400px] mx-auto p-15 box secao-input"
			style="background-color: #00428F;">
			<h3 class="text-3xl font-bold text-white titulo-secao">Faça seu login</h3>
			<div class="grid grid-cols-1 gap-1">

				<label class="block mb-1 font-semibold text-white texto-label">Digite seu email:</label>
				<input type="text" placeholder="" class="input input-bordered w-full  texto-opcoes"
					style="background-color: #FAFAFAE5;" />

			</div>
			<div class="grid grid-cols-1 gap-1">

				<label class="block mb-1 font-semibold text-white texto-label">Senha:</label>
				<input type="text" placeholder="" class="input input-bordered w-full  texto-opcoes"
					style="background-color: #FAFAFAE5;" />

			</div>

			<button class="botao-login">
				Fazer login
			</button>
			<router-link to="/auth/esqueci-senha">
				<p class="link-recadastro-senha">Esqueceu sua senha ou email cadastrado?</p>
			</router-link>

		</div>
	</section>

	<Footer />


</template>

<script setup lang="ts">
import { Route } from 'lucide-vue-next';
import { RouterLink } from 'vue-router';
import NavBarHome from '@/components/baseUi/NavBarHome.vue'
import Footer from '@/components/baseUi/Footer.vue'

RouterLink
</script>

<style scoped>
.secao-texto {
	transform: rotate(90deg);
	z-index: 1;
	color: #ffffff;
}

.texto-bem-vindos {
	font-family: 'Open Sans', sans-serif;
	font-size: 75px;
	position: relative;
	bottom: -150px;
}

.secao-bem-vindos {
	background-color: #00428F80;
	width: 900px;
	height: 780px;
	border-radius: 69px;
	position: absolute;
}

.primeira-div {
	transform: rotate(64deg);
	left: -350px;
	top: -60px;
}

.segunda-div {
	transform: rotate(-132deg);
	left: -350px;
	top: -73px;

}

.secao-login {
	margin-top: 10rem;
	display: flex;
	align-items: center;
	justify-content: center;
	gap: 13rem;
	margin-bottom: 5rem;
}

.secao-input {
	padding: 3rem 1rem;
	width: 400px;
	display: flex;
	flex-direction: column;
	gap: 2rem;

}

.titulo-secao {
	font-family: 'Open Sans', sans-serif;
	font-size: 38px;
	text-align: center;

	font-weight: 400;
}

.texto-label {
	font-family: 'Open Sans', sans-serif;
	font-size: 16px;
	font-weight: 400;
	color: #FAFAFA;
}

.botao-login {
	background-color: #E1E7EF;
	color: #002A5C;
	padding: 10px 20px;
	border: none;
	border-radius: 5px;
	cursor: pointer;
	width: fit-content;
	font-family: 'Open Sans', sans-serif;
}

.link-recadastro-senha {
	color: #FAFAFA;
}
</style>