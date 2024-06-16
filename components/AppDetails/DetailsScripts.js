export default {
    setDetailsPosition(elem) {
        const windowWidth = document.documentElement.clientWidth
        const windowHeight = document.documentElement.clientHeight
        const detailsRect = elem.getBoundingClientRect()
        const detailsContentRect = elem.querySelector('.details__content').getBoundingClientRect()

        if (detailsContentRect.height + detailsRect.top > windowHeight) {
            elem.classList.add('details_top')
        } else {
            elem.classList.remove('details_top')
        }
        
        if (detailsContentRect.right > windowWidth) {
            elem.classList.add('details_left')
        } else {
            elem.classList.remove('details_left')
        }
    }
}