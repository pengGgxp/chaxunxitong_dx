$(document).ready(function () {
    // 获取所有带有倒计时的元素
    var countdownElements = $('.countdown');

    // 对每个元素进行处理
    countdownElements.each(function () {
        var targetTime = $(this).data('time');

        // 更新倒计时函数
        function updateCountdown() {
            var currentTime = new Date().getTime();
            var timeDifference = new Date(targetTime) - currentTime;

            // 计算时、分、秒
            var seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);
            var minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
            var hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            var days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
            // 更新元素的文本内容
            $(this).text(days + "天" + hours + "时" + minutes + "分" + seconds + '秒');

            // 如果倒计时结束，可以执行相应的操作，比如隐藏元素
            if (timeDifference <= 0) {
                $(this).text("倒计时结束");
                // 可以添加其他逻辑
            }
        }

        // 初始调用一次，确保页面加载时显示正确的倒计时
        updateCountdown.call(this);

        // 设置定时器，每秒更新一次倒计时
        setInterval(updateCountdown.bind(this), 1000);
    });

    var title_date = $('.day-title');
    title_date.each(function () {
        function title_time() {
            var currentDate = new Date();
            var year = currentDate.getFullYear();
            var month = (currentDate.getMonth() + 1).toString().padStart(2, '0'); // 月份从0开始，需要加1，并确保是两位数
            var day = currentDate.getDate().toString().padStart(2, '0');
            var hours = currentDate.getHours().toString().padStart(2, '0');
            var minutes = currentDate.getMinutes().toString().padStart(2, '0');
            var seconds = currentDate.getSeconds().toString().padStart(2, '0');
            $(this).text(year + '年' + month + '月' + day + '日' + hours + '时' + minutes + '分' + seconds + '秒');
        }
        title_time.call(this);

        setInterval(title_time.bind(this),1000);

    });
});