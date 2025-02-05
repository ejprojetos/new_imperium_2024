<template>
    <NavBarHome />
    <section class="secao-login">
        <div class="secao-texto">
            <h1 class="texto-bem-vindos">REDEFINIR SENHA</h1>
        </div>
        <div>
            <div class="secao-bem-vindos primeira-div"></div>
            <div class="secao-bem-vindos segunda-div"></div>
        </div>

        <div
            class="p-6 rounded-lg shadow-lg max-w-[400px] mx-auto p-15 box secao-input"
            style="background-color: #00428f">
            <h3 class="text-3xl font-bold text-white titulo-secao">Esqueci minha senha</h3>

            <div v-if="errorMessage" class="mb-4 alert alert-error">
                {{ errorMessage }}
            </div>

            <div v-if="successMessage" class="mb-4 alert alert-success">
                {{ successMessage }}
            </div>

            <div class="grid grid-cols-1 gap-1">
                <label class="block mb-1 font-semibold text-white texto-label">
                    Digite seu e-mail para redefinir sua senha:
                </label>
                <input
                    v-model="email"
                    type="email"
                    placeholder="seu@email.com"
                    class="w-full input input-bordered texto-opcoes"
                    style="background-color: #fafafae5" />
            </div>

            <div class="secao-botao">
                <button @click="handlePasswordReset" class="botao-login" :disabled="loading">
                    {{ loading ? 'ENVIANDO...' : 'ENVIAR EMAIL' }}
                </button>
            </div>
        </div>
    </section>
    <Footer />
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import NavBarHome from '@/components/baseUi/NavBarHome.vue'
import Footer from '@/components/baseUi/Footer.vue'
import { authService } from '@/services/auth.service'

const router = useRouter()
const email = ref('')
const loading = ref(false)
const errorMessage = ref('')
const successMessage = ref('')

const handlePasswordReset = async () => {
    if (!email.value) {
        errorMessage.value = 'por favor, insira seu email'
        return
    }

    loading.value = true
    errorMessage.value = ''
    successMessage.value = ''

    try {
        await authService.requestPasswordReset(email.value)
        successMessage.value = 'Email de recuperação enviado com sucesso'
        setTimeout(() => {
            router.push('/auth/email-enviado')
        }, 2000)
    } catch (error: any) {
        errorMessage.value = error.message || 'Erro ao solicitar recuperação de senha'
    } finally {
        loading.value = false
    }
}
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
    bottom: -220px;
}

.secao-bem-vindos {
    background-color: #00428f80;
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
    margin-top: 15rem;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8rem;
    margin-bottom: 12rem;
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
    font-size: 36px;
    text-align: center;

    font-weight: 400;
}

.texto-label {
    font-family: 'Open Sans', sans-serif;
    font-size: 16px;
    font-weight: 400;
    color: #fafafa;
}

.secao-botao {
    display: flex;
    justify-content: center;
}

.botao-login {
    background-color: #e1e7ef;
    color: #002a5c;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    width: fit-content;
    font-family: 'Open Sans', sans-serif;
    font-family: Raleway;
    font-size: 15px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
}

.link-recadastro-senha {
    color: #fafafa;
}
</style>
