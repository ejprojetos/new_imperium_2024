<template>
    <swiper
      :spaceBetween="30"
      :centeredSlides="true"
      :autoplay="{
        delay: 2500,
        disableOnInteraction: false
      }"
      :pagination="{
        clickable: true
      }"
      :navigation="false"
    >
      <!-- Gerando os slides dinamicamente usando v-for -->
      <swiper-slide v-for="(item, index) in slides" :key="index" class="h-full flex justify-center items-center rounded-lg mt-[75px]">
        <div class="flex flex-col items-center text-center h-[390px]">
          <img v-if="item.image" :src="item.image" class="w-[150px] h-[150px] object-cover rounded-full" />
          <div>
              <p class="font-roboto mt-[30px] w-[1196px]">{{ item.description }}</p>
          </div>
        </div>
      </swiper-slide>
    </swiper>
  </template>
  
  <script lang="ts">
  import { defineComponent } from "vue";
  import { Swiper, SwiperSlide } from "swiper/vue";
  import 'swiper/swiper-bundle.css';
  import 'swiper/css/pagination'; 
  import "swiper/css/navigation";
  import SwiperCore from "swiper";
  import { Pagination, Navigation, Autoplay } from "swiper/modules";
  
  SwiperCore.use([Autoplay, Pagination, Navigation]);
  
  export default defineComponent({
    name: "CarroselInstitucional",
    components: {
      Swiper,
      SwiperSlide
    },
    data() {
      return {
        // Lista de slides
        slides: [
          {description: "Praesent est mi, consequat sed aliquam in, ornare quis neque. Integer euismod libero eu nibh blandit molestie. Sed faucibus, est ac tincidunt feugiat, eros ligula varius nibh, nec vestibulum nunc orci sit amet odio.. ", image: "../src/assets/images/romulo.png" },
          {description: "Praesent est mi, consequat sed aliquam in, ornare quis neque. Integer euismod libero eu nibh blandit molestie. Sed faucibus, est ac tincidunt feugiat, eros ligula varius nibh, nec vestibulum nunc orci sit amet odio.", image: "../src/assets/images/pedro.png" },
          {description: "Praesent est mi, consequat sed aliquam in, ornare quis neque. Integer euismod libero eu nibh blandit molestie. Sed faucibus, est ac tincidunt feugiat, eros ligula varius nibh, nec vestibulum nunc orci sit amet odio.", image: "../src/assets/images/depoiments.png" },
          {description: "Praesent est mi, consequat sed aliquam in, ornare quis neque. Integer euismod libero eu nibh blandit molestie. Sed faucibus, est ac tincidunt feugiat, eros ligula varius nibh, nec vestibulum nunc orci sit amet odio.", image: "../src/assets/images/depoiments.png" },
          {description: "Praesent est mi, consequat sed aliquam in, ornare quis neque. Integer euismod libero eu nibh blandit molestie. Sed faucibus, est ac tincidunt feugiat, eros ligula varius nibh, nec vestibulum nunc orci sit amet odio.", image: "../src/assets/images/depoiments.png" }
        ]
      };
    }
  });
  </script>
  
  <style scoped>
  /* Customizing Swiper styles with Tailwind */
  .swiper-container {
    width: 100%;
    height: 100%;
  }
  
  .swiper-slide {
    text-align: center;
    font-size: 18px;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .swiper-pagination {
  position: absolute;
  bottom: 71px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  z-index: 10;
}
  
  </style>
  