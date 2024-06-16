<template>
    <div class="resume__header resume-header">
        <div class="resume-header__personal personal">
            <figure class="personal__avatar">
                <img src="~/assets/img/json.jpg" alt="avatar">
            </figure>
            <div class="personal__info personal-info">
                <div class="personal-info__item personal-info__item_name">
                    <h3 class="personal-info__item-name">Стетхем Стет Стетхомович </h3>
                    <p class="personal-info__item-status">Активно ищу работу</p>
                </div>

                <div class="personal-info__item personal-info__item_edit">
                    <div class="personal-info__text">
                        <p>Мужчина, 99 лет, Дата рождения - 17.02.2000</p>
                        <p>Москва, м. Тульская, не готов к переезду, готов к командировкам</p>
                    </div>
                    <ResumeEditItem class="personal-info__icon-edit" />
                </div>
            </div>
        </div>
        <div class="resume-header__actions actions">
            <AppButton class="actions__button"><Install /></AppButton>
            <AppButton class="actions__button"><Trash /></AppButton>
        </div>

        <span class="resume-header__updated">Резюме обновлено 05.06.2024 11:44</span>
    </div>

</template>

<script setup>
    import './ResumeHeader.scss'

    import ResumeEditItem from "~/components/ApplicantComponents/Resume/ResumeEditItem/ResumeEditItem.vue";
    import Install from "~/components/AppIcons/Install.vue";
    import Trash from "~/components/AppIcons/Trash.vue";

</script>