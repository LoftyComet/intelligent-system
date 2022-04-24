
function optBtnHandler(e){
    var optType = $(this).attr("opttype");
    var dataId = $(this).attr("dataId");
    if(optType == "editUser"){
        var username = $(this).attr("username");
        $("#edit_user_id").val(dataId);
        $("#edit_user_fullname").val(username);
        var myModal = new bootstrap.Modal(document.getElementById('edit_user_modal'), {
          keyboard: false
        });
        myModal.show();
    }
    else if(optType == "deleteUser"){
        var username = $(this).attr("username");
        var isconfirm = confirm("您确定删除用户“"+username+"”吗？")
        if(isconfirm){
            $.post('/user',
                {
                    "type": 'delete',
                    "id":dataId
                },
                function (callback) {
                    window.location.reload();
                })
        }
    }
    else if(optType == "editCar"){
        // console.log("111");
        var light = $(this).attr("light");
        var traffic = $(this).attr("traffic");
        var time = $(this).attr("time");
        $("#edit_car_id").val(dataId);
        $("#edit_car_light").val(light);
        $("#edit_car_traffic").val(traffic);
        $("#edit_car_time").val(time);
        var myModal = new bootstrap.Modal(document.getElementById('edit_car_modal'), {
          keyboard: false
        });
        myModal.show();
        }
    else if(optType == "deleteCar"){
        var time = $(this).attr("time");
        $("#edit_car_id").val(dataId);
        var isconfirm = confirm("您确定删除“"+time+"”时段的车流量记录吗？")
        if(isconfirm){
            $.post('/car',
                {
                    "type": 'delete',
                    "id":dataId
                },
                function (callback) {
                    window.location.reload();
                })
        }
    }
}

function onAddUserClickHandler(e){
    var myModal = new bootstrap.Modal(document.getElementById('add_user_modal'), {
      keyboard: false
    })
    myModal.show()
}

function onAddUserSubmitClickHandler(e){
    var myModal = new bootstrap.Modal(document.getElementById('add_user_modal_show_btn'), {
      keyboard: false
    })
    var fullname = $("#fullname").val();
    $.post('/user',
        {
            "type": 'add',
            "username": $("#fullname").val()
        },
        function (callback) {
            window.location.reload();
        })
    myModal.hide()
}


function onEidtUserSubmitClickHandler(e){
    var myModal = new bootstrap.Modal(document.getElementById('add_user_modal_show_btn'), {
      keyboard: false
    })
    var fullname = $("#edit_user_fullname").val();
    var id = $("#edit_user_id").val();
    $.post('/user',
        {
            "type": 'edit',
            "username": fullname,
            "id":id
        },
        function (callback) {
            window.location.reload();
        })


    myModal.hide()
}

// 下面是车流量的增删改查
function onAddCarClickHandler(e){
    // console.log("我被点击了");
    var myModal = new bootstrap.Modal(document.getElementById('add_car_modal'), {
      keyboard: false
    })
    myModal.show()
}

function onAddCarSubmitClickHandler(e){
    var myModal = new bootstrap.Modal(document.getElementById('add_car_modal_show_btn'), {
      keyboard: false
    })
    var light = $("#add_car_light").val();
    var traffic = $("#add_car_traffic").val();
    var time = $("#add_car_time").val();
    console.log("点击了添加");
    $.post('/car',
        {
            "type": 'add',
            "light": light,
            "traffic": traffic,
            "time": time,
        },
        function (callback) {
            window.location.reload();
        })


    myModal.hide()
}

function onEidtCarSubmitClickHandler(e){
    var myModal = new bootstrap.Modal(document.getElementById('add_car_modal_show_btn'), {
      keyboard: false
    })
    var light = $("#edit_car_light").val();
    var traffic=$("#edit_car_traffic").val();
    var time=$("#edit_car_time").val();
    var id = $("#edit_car_id").val();
    $.post('/car',
        {
            "type": 'edit',
            "light": light,
            "traffic": traffic,
            "time": time,
            "id":id
        },
        function (callback) {
            window.location.reload();
        })
    myModal.hide()
}

$(document).ready(function(){
    $('#add_user_modal_show_btn').click(onAddUserClickHandler);
    $("#add_user_submit").click(onAddUserSubmitClickHandler);
    $("#edit_user_submit").click(onEidtUserSubmitClickHandler);
    $(".optbtn").click(optBtnHandler);


    $("#edit_car_submit").click(onEidtCarSubmitClickHandler);
    $('#add_car_modal_show_btn').click(onAddCarClickHandler);
    $("#add_car_submit").click(onAddCarSubmitClickHandler);


})

