<template>
    <ion-page>
        <ion-content class="ion-padding">
            <div class="not-found-container">
                <h1>404</h1>
                <h2>Ops! Página não encontrada</h2>
                <RouterLink class="mt-4" to="/dashboard">
                    <button class="btn btn-wide">Voltar para o Dashboard</button>
                </RouterLink>
            </div>
        </ion-content>
    </ion-page>
</template>
<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.not-found-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    text-align: center;
}

h1 {
    font-size: 6rem;
    margin-bottom: 0;
}

h2 {
    font-size: 2rem;
    margin-top: 0;
}
</style>