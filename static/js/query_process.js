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
        var submitBtn = document.getElementById('submit_btn');
        var submitBtnLoad = document.getElementById('submit_btn_load');
         // 禁用按钮
    submitBtn.disabled = true;

    // 显示加载中的样式
    submitBtnLoad.classList.remove('d-none');

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
                var resultContainer = document.getElementById('result-container');
                resultContainer.innerHTML = '';
                var id_count = 0;
                var iiid = '';

                if (querymode === "xuexiao") {
                    // JSON.parse(response);
                    var data_xuexiao = response;
                    // console.log(data_xuexiao)
                    for (var key in data_xuexiao) {
                        if (data_xuexiao.hasOwnProperty(key)) {
                            var item = data_xuexiao[key];
                            var itemDiv1 = document.createElement('div');


                            itemDiv1.style.border = '1px solid #ccc';
                            itemDiv1.style.margin = '10px';
                            itemDiv1.style.padding = '10px';
                            itemDiv1.classList.add('cx-card')

                            var htmlContent = '<div class="mb-3"><strong>学校名称:</strong> ' + item.xuexiaomingcheng + '</div>';
                            htmlContent += '<div class="mb-3"><strong>办学性质:</strong> ' + item.beizhu + '</div>';

                            // 遍历data数组
                            for (var i = 0; i < item.data.length; i++) {
                                var entry = item.data[i];
                                // htmlContent += '<div style="border: 1px solid rgb(204, 204, 204); margin: 10px; padding: 10px;">';
                                htmlContent += '<div class="card cx-content-only-card">';
                                htmlContent += '<div class="card-header">';
                                iiid = "collapse_" + id_count;
                                // console.log("iiid:",iiid);
                                id_count++;
                                htmlContent += '<a class="btn" data-bs-toggle="collapse" href="' + '#' +iiid + '">';
                                htmlContent += '<div class="text-black">' + entry.zhuanyemingcheng + '</div>';
                                htmlContent += '</a>';
                                htmlContent += '</div>';
                                htmlContent += '<div id="' + iiid + '" class="collapse hide" data-bs-parent="#result-container">';
                                htmlContent += '<div class="card-body">';
                                htmlContent += '<div class="mb-3"><strong>招生计划:</strong> ' + entry.zhaoshengjihua + '</div>';
                                htmlContent += '<div class="mb-3"><strong>学费:</strong> ' + entry.xuefei + '</div>';
                                htmlContent += '<div class="mb-3"><strong>招生类型:</strong> ' + entry.zhaoshengleixing + '</div>';
                                htmlContent += '<div class="mb-3"><strong>性质:</strong> ' + entry.xingzhi + '</div>';
                                htmlContent += '<div class="mb-3"><strong>年份:</strong> ' + entry.nianfen + '</div>';
                                htmlContent += '<div class="mb-3"><strong>专业类别:</strong> ' + entry.zhuanyeleibie + '</div>';
                                htmlContent += '<div class="mb-3"><strong>可报志愿数量:</strong> ' + entry.kebaozhiyuansl + '</div>';
                                htmlContent += '<div class="mb-3"><strong>考试内容:</strong> ' + entry.kaoshineirong + '</div>';
                                htmlContent += '<div class="mb-3"><strong>考试方式:</strong> ' + entry.kaoshifangshi + '</div>';
                                htmlContent += '</div>';
                                htmlContent += '</div>';
                                htmlContent += '</div>';
                                // htmlContent += '</div>';
                            }

                            // 将htmlContent添加到itemDiv1中
                            itemDiv1.innerHTML = htmlContent;
                            // 将itemDiv1添加到body中
                            resultContainer.appendChild(itemDiv1);
                        }
                    }

                } else if (querymode === "zhuanye") {
                    var data_zhuanye = response;
                    // console.log(data_zhuanye)

                    for (var key2 in data_zhuanye) {
                        if (data_zhuanye.hasOwnProperty(key2)) {
                            var item2 = data_zhuanye[key2];
                            var itemDiv2 = document.createElement('div');


                            itemDiv2.style.border = '1px solid #ccc';
                            itemDiv2.style.margin = '10px';
                            itemDiv2.style.padding = '10px';
                            itemDiv2.classList.add('cx-card')
                            var htmlContent2 = '';

                            // 遍历data数组
                            for (var i2 = 0; i2 < item2.data.length; i2++) {
                                var entry2 = item2.data[i2];
                                // htmlContent2 += '<div style="border: 1px solid rgb(204, 204, 204); margin: 10px; padding: 10px;">';
                                htmlContent2 += '<div class="card cx-content-only-card">';
                                htmlContent2 += '<div class="card-header">';
                                iiid = "collapse_" + id_count;
                                // console.log("iiid:",iiid);
                                id_count++;
                                htmlContent2 += '<a class="btn" data-bs-toggle="collapse" href="' + '#' +iiid + '">';
                                htmlContent2 += '<div class="text-black"> ' + entry2.zhuanyemingcheng + '</div>';
                                htmlContent2 += '</a>';
                                htmlContent2 += '</div>';
                                htmlContent2 += '<div id="' + iiid + '" class="collapse hide" data-bs-parent="#result-container">';
                                htmlContent2 += '<div class="card-body">';
                                htmlContent2 += '<div class="mb-3"><strong>招生计划:</strong> ' + entry2.zhaoshengjihua + '</div>';
                                htmlContent2 += '<div class="mb-3"><strong>学费:</strong> ' + entry2.xuefei + '</div>';
                                htmlContent2 += '<div class="mb-3"><strong>招生类型:</strong> ' + entry2.zhaoshengleixing + '</div>';
                                htmlContent2 += '<div class="mb-3"><strong>性质:</strong> ' + entry2.xingzhi + '</div>';
                                htmlContent2 += '<div class="mb-3"><strong>年份:</strong> ' + entry2.nianfen + '</div>';
                                htmlContent2 += '<div class="mb-3"><strong>专业类别:</strong> ' + entry2.zhuanyeleibie + '</div>';
                                htmlContent2 += '<div class="mb-3"><strong>可报志愿数量:</strong> ' + entry2.kebaozhiyuansl + '</div>';
                                htmlContent2 += '<div class="mb-3"><strong>考试内容:</strong> ' + entry2.kaoshineirong + '</div>';
                                htmlContent2 += '<div class="mb-3"><strong>考试方式:</strong> ' + entry2.kaoshifangshi + '</div>';
                                // htmlContent2 += '</div>';
                                htmlContent2 += '</div>';
                                htmlContent2 += '</div>';
                                htmlContent2 += '</div>';
                            }

                            htmlContent2 += '<div class="mb-3 mt-3"><strong>学校名称:</strong> ' + item2.xuexiaomingcheng + '</div>';
                            htmlContent2 += '<div class="mb-3"><strong>办学性质:</strong> ' + item2.beizhu + '</div>';

                            // 将htmlContent添加到itemDiv1中
                            itemDiv2.innerHTML = htmlContent2;
                            // 将itemDiv1添加到body中
                            resultContainer.appendChild(itemDiv2);
                        }
                    }
                }


            },
            error: function (error) {
                console.error('Error:', error)
            }

        })

         // 启用按钮
        submitBtn.disabled = false;

        // 隐藏加载中的样式
        submitBtnLoad.classList.add('d-none');
    })
})

function showxuexiaosou() {
    $('#xuexiaomode').removeClass('d-none');
    $('#zhuanyemode').addClass('d-none');
    $('#anxuexiaosou').removeClass().addClass('btn btn-primary');
    $('#anzhuanyesou').removeClass().addClass('btn btn-secondary');
}

function showzhuanyesou() {
    $('#xuexiaomode').addClass('d-none');
    $('#zhuanyemode').removeClass('d-none');
    $('#anxuexiaosou').removeClass().addClass('btn btn-secondary');
    $('#anzhuanyesou').removeClass().addClass('btn btn-primary');

}


function getsubmiturl(querymode) {
    if (querymode === 'xuexiao') {
        return 'query/xuexiao/'
    } else if (querymode === 'zhuanye') {
        return 'query/zhuanye/'
    }
}
