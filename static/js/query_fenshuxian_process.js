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
        query_benkefenshuxian(querymode);
    })
    query_benkefenshuxian(querymode);
})

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

function query_benkefenshuxian(querymode) {
    var submitBtn = document.getElementById('submit_btn');
    var submitBtnLoad = document.getElementById('submit_btn_load');
    submitBtn.disabled = true;
    submitBtnLoad.classList.remove('d-none');


    var select_nianfen = $("select[name='nianfen']").val();
    var select_banxuexingzhi = [];
    $("input[name='banxuexingzhi']:checkbox").each(function () {
        if ($(this).prop('checked')) {
            select_banxuexingzhi.push($(this).val());
        }
    })
    var select_zhuanyeleibie = $("select[name='zhuanyeleibie']").val();
    var select_fenshu = $("input[name='fenshu']").val();
    var select_weici = $("input[name='weici']").val();
    var select_mingcheng = '';
    if (querymode === 'xuexiao') {
        select_mingcheng = $("input[name='xuexiaomingcheng']").val();
    } else if (querymode === 'zhuanye') {
        select_mingcheng = $("input[name='zhuanyemingcheng']").val();
    }
    var select_zhuan_ben = $("input[name='zhuan_ben']").val();

    var data_send = {
        querymode: querymode,
        nianfen: select_nianfen,
        banxuexingzhi: select_banxuexingzhi,
        zhuanyeleibie: select_zhuanyeleibie,
        fenshu: select_fenshu,
        weici: select_weici,
        mingcheng: select_mingcheng,
        zhuan_ben: select_zhuan_ben,
    }
    $.ajax({
        url: '/query/fenshuxian/',
        type: 'POST',
        dataType: 'json',
        data: data_send,
        headers:
            {
                "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val(),
            },
        success:function (response) {
            var resultContainer = document.getElementById('result-container');
            resultContainer.innerHTML = '';
            var id_count = 0;
            var iiid = '';
            console.log(response)
        }
    })


    submitBtn.disabled = false;
    submitBtnLoad.classList.add('d-none');
}