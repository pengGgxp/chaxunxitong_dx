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
        query_cx_danzhao(querymode);
    })
    query_cx_danzhao(querymode);
})


function query_cx_danzhao(querymode) {
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
            select_banxuexingzhi.push($(this).val());
        }

    })
    var select_kaoshifangshi = [];
    $("input[name='kaoshifangshi']:checkbox").each(function () {
        if ($(this).prop('checked')) {
            select_kaoshifangshi.push($(this).val());
        }

    })
    var select_mingcheng = '';
    if (querymode === 'xuexiao') {
        select_mingcheng = $("input[name='xuexiaomingcheng']").val();
    } else if (querymode === 'zhuanye') {
        select_mingcheng = $("input[name='zhuanyemingcheng']").val();
    }

    var data_send = {
        querymode: querymode,
        zhaoshengleixing: select_zhaoshengleixing,
        nianfen: select_nianfen,
        banxuexingzhi: select_banxuexingzhi,
        kaoshifangshi: select_kaoshifangshi,
        mingcheng: select_mingcheng,
    };

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
                        itemDiv1.classList.add('cx-card', 'border-cx', 'mb-3', 'p-2');

                        var htmlContent = '<div class="card mb-3 mt-3 px-2">';
                        htmlContent += '<div class="d-flex align-content-center justify-content-between danzhaocx-xuexiao-card-xuexiao mb-1 ">';
                        htmlContent += '<div class="my-3"><strong>学校名称:</strong> ' + item.xuexiaomingcheng_xuexiaomingcheng + '</div>';
                        if (item.beizhu_xuexiaomingcheng === '民办') {
                            htmlContent += '<div class="my-3 me-3 round-xz-mb px-3 text-white small my-auto"> <strong>' + item.beizhu_xuexiaomingcheng + '</strong></div>';
                        } else {
                            htmlContent += '<div class="my-3 me-3 round-xz px-3 text-white small my-auto"> <strong>' + item.beizhu_xuexiaomingcheng + '</strong></div>';
                        }

                        htmlContent += '</div>';

                        htmlContent += '<div class="d-flex flex-column mb-3">';
                        if (item.beizhu_xuexiaomingcheng === '民办') {
                            htmlContent += '<div class="d-flex flex-fill flex-row align-content-center justify-content-between danzhaocx-xuexiao-card-header-mb text-white mt-3">';
                        } else {
                            htmlContent += '<div class="d-flex flex-fill flex-row align-content-center justify-content-between danzhaocx-xuexiao-card-header text-white mt-3">';
                        }
                        htmlContent += '<div><strong>考试方式:</strong>' + item.kaoshifangshi + '</div>';
                        htmlContent += '<div><strong>可报志愿数量:</strong> ' + item.kebaozhiyuansl + '</div>';

                        htmlContent += '</div>';
                        if (item.beizhu_xuexiaomingcheng === '民办') {
                            htmlContent += '<div class="danzhaocx-xuexiao-card-content pt-3"><strong style="color: #e92b2b">考试内容<span class="triangle ps-1"><i class="fas fa-caret-down"></i></span></strong><br> ' + item.kaoshineirong + '</div>';
                        } else {
                            htmlContent += '<div class="danzhaocx-xuexiao-card-content pt-3"><strong style="color: #2b5be9">考试内容<span class="triangle ps-1"><i class="fas fa-caret-down "></i></span></strong><br> ' + item.kaoshineirong + '</div>';
                        }
                        htmlContent += '</div>';
                        htmlContent += '</div>';

                        for (var i = 0; i < item.data.length; i++) {
                            var entry = item.data[i];
                            iiid = "collapse_" + id_count;
                            htmlContent += '<div class="card my-3">';
                            htmlContent += '<div class="card-header">';
                            htmlContent += '<a class="btn d-flex flex-fill flex-row align-content-center justify-content-between px-0" data-bs-toggle="collapse" href="#' + iiid + '">';
                            htmlContent += '<div class="text-black "><strong>' + entry.zhuanyemingcheng + '</strong></div>';
                            htmlContent += '<div class=""><strong>专业类别:</strong> ' + entry.zhuanyeleibie + '</div>';
                            htmlContent += '</a>';
                            htmlContent += '</div>';
                            htmlContent += '<div id="' + iiid + '" class="collapse show">';
                            htmlContent += '<div class="card-body d-flex flex-fill flex-row align-content-center justify-content-between px-3 pb-0">';
                            htmlContent += '<div class="mb-3"><strong>招生计划:</strong> ' + entry.zhaoshengjihua + '</div>';
                            htmlContent += '<div class="mb-3"><strong>学费:</strong> ' + entry.xuefei + '</div>';
                            htmlContent += '<div class="mb-3"><strong>招生类型:</strong> ' + entry.zhaoshengleixing + '</div>';
                            htmlContent += '</div>';
                            htmlContent += '</div>';
                            htmlContent += '</div>';
                            id_count++;
                        }

                        itemDiv1.innerHTML = htmlContent;
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
                        itemDiv2.classList.add('cx-card', 'border-cx', 'mb-3', 'p-2');

                        var htmlContent2 = '';
                        for (var i2 = 0; i2 < item2.data.length; i2++) {
                            var entry2 = item2.data[i2];
                            iiid = "collapse_" + id_count;
                            id_count++;
                            htmlContent2 += '<div class="card">';
                            htmlContent2 += '<div class="card-header">';
                            htmlContent2 += '<a class="btn d-flex flex-fill flex-row align-content-center justify-content-between px-0" data-bs-toggle="collapse" href="#' + iiid + '">';
                            htmlContent2 += '<div class="text-black "><strong>' + entry2.zhuanyemingcheng + '</strong></div>';
                            htmlContent2 += '<div class=""><strong>专业类别:</strong> ' + entry2.zhuanyeleibie + '</div>';
                            htmlContent2 += '</a>';
                            htmlContent2 += '</div>';
                            htmlContent2 += '<div id="' + iiid + '" class="collapse show">';
                            htmlContent2 += '<div class="card-body d-flex flex-fill flex-row align-content-center justify-content-between px-3 pb-0">';
                            htmlContent2 += '<div class="mb-3"><strong>招生计划:</strong> ' + entry2.zhaoshengjihua + '</div>';
                            htmlContent2 += '<div class="mb-3"><strong>学费:</strong> ' + entry2.xuefei + '</div>';
                            htmlContent2 += '<div class="mb-3"><strong>招生类型:</strong> ' + entry2.zhaoshengleixing + '</div>';
                            htmlContent2 += '</div>';
                            htmlContent2 += '</div>';
                            htmlContent2 += '</div>';

                            htmlContent2 += '<div class="card mb-3 mt-3 px-2">';
                            htmlContent2 += '<div class="d-flex align-content-center justify-content-between danzhaocx-xuexiao-card-xuexiao mb-1">';
                            htmlContent2 += '<div class="my-3"><strong>学校名称:</strong> ' + entry2.xuexiaomingcheng_xuexiaomingcheng + '</div>';
                            if (entry2.beizhu_xuexiaomingcheng === '民办') {
                                htmlContent2 += '<div class="my-3 me-3 round-xz-mb px-3 text-white small my-auto"> <strong>' + entry2.beizhu_xuexiaomingcheng + '</strong></div>';
                            } else {
                                htmlContent2 += '<div class="my-3 me-3 round-xz px-3 text-white small my-auto"> <strong>' + entry2.beizhu_xuexiaomingcheng + '</strong></div>';
                            }
                            htmlContent2 += '</div>';
                            htmlContent2 += '<div class="d-flex flex-column mb-3">';
                            if (entry2.beizhu_xuexiaomingcheng === '民办') {
                                htmlContent2 += '<div class="d-flex flex-fill flex-row align-content-center justify-content-between danzhaocx-xuexiao-card-header-mb text-white mt-3">';
                            } else {
                                htmlContent2 += '<div class="d-flex flex-fill flex-row align-content-center justify-content-between danzhaocx-xuexiao-card-header  text-white mt-3">';
                            }
                            htmlContent2 += '<div><strong>考试方式:</strong> ' + entry2.kaoshifangshi + '</div>';
                            htmlContent2 += '<div><strong>可报志愿数量:</strong> ' + entry2.kebaozhiyuansl + '</div>';
                            htmlContent2 += '</div>';

                            if (entry2.beizhu_xuexiaomingcheng === '民办') {
                            htmlContent2 += '<div class="danzhaocx-xuexiao-card-content pt-3"><strong style="color: #e92b2b">考试内容<span class="triangle ps-1"><i class="fas fa-caret-down"></i></span></strong><br> ' + entry2.kaoshineirong + '</div>';
                        } else {
                            htmlContent2 += '<div class="danzhaocx-xuexiao-card-content pt-3"><strong style="color: #2b5be9">考试内容<span class="triangle ps-1"><i class="fas fa-caret-down"></i></span></strong><br> ' + entry2.kaoshineirong + '</div>';
                        }
                            htmlContent2 += '</div>';
                            htmlContent2 += '</div>';
                        }


                        itemDiv2.innerHTML = htmlContent2;
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
}

function showxuexiaosou() {
    $('#xuexiaomode').removeClass('d-none');
    $('#zhuanyemode').addClass('d-none');
    $('#anxuexiaosou').removeClass().addClass('btn btn-primary');
    $('#anzhuanyesou').removeClass().addClass('btn btn-light');
}

function showzhuanyesou() {
    $('#xuexiaomode').addClass('d-none');
    $('#zhuanyemode').removeClass('d-none');
    $('#anxuexiaosou').removeClass().addClass('btn btn-light');
    $('#anzhuanyesou').removeClass().addClass('btn btn-primary');
}


function getsubmiturl(querymode) {
    if (querymode === 'xuexiao') {
        return '/query/danzhao/xuexiao/'
    } else if (querymode === 'zhuanye') {
        return '/query/danzhao/zhuanye/'
    }
}
