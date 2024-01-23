$(document).ready(function () {
    showxuexiaosou();
    var querymode = "xuexiao";
    $("#anxuexiaosou").click(function () {
        showxuexiaosou();
        querymode = "xuexiao";
    })

    $("#anzhuanyesou").click(function () {
        showzhuanyesou();
        querymode = "zhuanye";
    })


    $("#submit_btn").click(function () {
        var select_zhaoshengleixing = $("select[name='zhaoshengleixing']").val();
        var select_nianfen = $("select[name='nianfen']").val();
        var select_banxuexingzhi = [];
        $("input[name='banxuexingzhi']:checkbox").each(function () {
            if ($(this).prop('checked')) {
                select_banxuexingzhi.push($(this).val())
            }

        })
        var select_kaoshifangshi = [];
        $("input[name='kaoshifangshi']:checkbox").each(function () {
            if ($(this).prop('checked')) {
                select_kaoshifangshi.push($(this).val())
            }

        })
        var select_mingcheng = '';
        if (querymode === 'xuexiao') {
        select_mingcheng = $("input[name='xuexiaomingcheng']").val()
    } else if (querymode === 'zhuanye') {
        select_mingcheng = $("input[name='zhuanyemingcheng']").val()
    }

        var data_send = {
            querymode: querymode,
            zhaoshengleixing: select_zhaoshengleixing,
            nianfen: select_nianfen,
            banxuexingzhi: select_banxuexingzhi,
            kaoshifangshi: select_kaoshifangshi,
            mingcheng: select_mingcheng,
        }

        $.ajax({
            url: getsubmiturl(querymode),
            type: 'POST',
            dataType: 'json',
            data: data_send,
            headers:
                {
                    "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val(),
                },
            success: function (response) {
                // console.log(response.jieguo)
                var data = JSON.parse(response.jieguo);
                var resultContainer = document.getElementById('result-container');
                resultContainer.innerHTML = '';
                data.zhaoshengxinxi.forEach(function (item) {
                    // 创建一个 div 元素用于显示每个条目的信息
                    var itemDiv = document.createElement('div');

                    // 设置元素的样式
                    itemDiv.style.border = '1px solid #ccc';
                    itemDiv.style.margin = '10px';
                    itemDiv.style.padding = '10px';

                    // 构建 HTML 内容
                    var htmlContent = '<div class="mb-3"><strong>学校名称:</strong> ' + item.xuexiaomingcheng + '</div>';
                    htmlContent += '<div class="mb-3"><strong>办学性质:</strong> ' + item.beizhu + '</div>';
                    htmlContent += '<div class="mb-3"><strong>专业名称:</strong> ' + item.zhuanyemingcheng + '</div>';
                    htmlContent += '<div class="mb-3"><strong>招生计划:</strong> ' + item.zhaoshengjihua + '</div>';
                    htmlContent += '<div class="mb-3"><strong>学费:</strong> ' + item.xuefei + '</div>';
                    htmlContent += '<div class="mb-3"><strong>招生类型:</strong> ' + item.zhaoshengleixing + '</div>';
                    htmlContent += '<div class="mb-3"><strong>性质:</strong> ' + item.xingzhi + '</div>';
                    htmlContent += '<div class="mb-3"><strong>年份:</strong> ' + item.nianfen + '</div>';
                    htmlContent += '<div class="mb-3"><strong>专业类别:</strong> ' + item.zhuanyeleibie + '</div>';
                    htmlContent += '<div class="mb-3"><strong>可报志愿数量:</strong> ' + item.kebaozhiyuansl + '</div>';
                    htmlContent += '<div class="mb-3"><strong>考试内容:</strong> ' + item.kaoshineirong + '</div>';
                    htmlContent += '<div class="mb-3"><strong>考试方式:</strong> ' + item.kaoshifangshi + '</div>';

                    // 将 HTML 内容添加到 div 元素中
                    itemDiv.innerHTML = htmlContent;

                    // 将 div 元素添加到结果容器中
                    resultContainer.appendChild(itemDiv);

                })

            },
            error: function (error) {
                console.error('Error:', error)
            }

        })


    })
})

function showxuexiaosou() {
    $('#xuexiaomode').show();
    $('#zhuanyemode').hide();
}

function showzhuanyesou() {
    $('#xuexiaomode').hide();
    $('#zhuanyemode').show();
}


function getsubmiturl(querymode) {
    if (querymode === 'xuexiao') {
        return 'query/xuexiao/'
    } else if (querymode === 'zhuanye') {
        return 'query/zhuanye/'
    }
}
