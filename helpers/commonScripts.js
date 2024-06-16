export default {
    differenceNumber(num1, num2) {
        return num1 > num2 ? num1 - num2 : num2 - num1
    },

    getNoun(number, one, two, five) {
        number = Math.abs(number)
        number %= 100
        if (number >= 5 && number <= 20) {
            return five
        }
        number %= 10
        if (number === 1) {
            return one
        }
        if (number >= 2 && number <= 4) {
            return two
        }
        return five
    },

    getNounMonth(number) {
        return this.getNoun(number, 'месяц', 'месяца', 'месяцев')
    },

    getNounYear(number) {
        return this.getNoun(number, 'год', 'года', 'лет')
    },

    formatDate(date) {
        let dd = date.getDate();
        if (dd < 10) dd = '0' + dd;

        let mm = date.getMonth() + 1;
        if (mm < 10) mm = '0' + mm;

        let yy = date.getFullYear() % 100;
        if (yy < 10) yy = '0' + yy;

        return dd + '.' + mm + '.' + yy;
    },

    compareArrays(arr1, arr2) {
        const sortArr1 = [...arr1].sort()
        const sortArr2 = [...arr2].sort()
        return JSON.stringify(sortArr1) === JSON.stringify(sortArr2)
    }
}