$(document).ready(function () {

//    function getCookie(name) {
//        var cookieValue = null;
//        if (document.cookie && document.cookie != '') {
//            var cookies = document.cookie.split(';');
//            for (var i = 0; i < cookies.length; i++) {
//                var cookie = jQuery.trim(cookies[i]);
//                // Does this cookie string begin with the name we want?
//                if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                    break;
//                }
//            }
//        }
//        return cookieValue;
//    }
//    $.ajaxSetup({
//      beforeSend: function(xhr, settings){
//
//          xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));//request头需要添加csrftoken,告诉服务器，我是个好yin哪，我是正常访问者
//      }
//    });

    var mailContentUm = UM.getEditor('mailContent');

    //根据noticeTypeTab显示邮件或短信页
    var noticeTypeTab = $('#noticeTypeTab').val();
    if (noticeTypeTab && noticeTypeTab == '1') {
        $('#send_sms_tab').click();
    }

    loadMailReceiver('#receiverId', '请选择收件人');
    loadMailReceiver('#copyReceiverId', '请选择抄送人');
    loadSmsReceiver('#smsReceiver', '请选择收件人');
    loadMailReceiver('#queryReceiverid', '请选择收件人');
    loadMailReceiver('#queryCopyReceiverId', '请选择收件人');


    //初始化收件人
    if ($('#receiverId').val()) {
        $.getJSON("http://127.0.0.1:9000/user/getByUserNames", {"userName": $('#receiverId').val()}, function (jsonData) {
            if (jsonData.length <= 0) {
                return;
            }
            var datas = [];
            for (var i = 0; i < jsonData.length; i++) {
                datas.push({
                    id: jsonData[i].userName,
                    text: jsonData[i].userCnName
                });
            }
            //处理自己输入的邮箱
            var receiverIdVal = $('#receiverId').val();
            receiverIdVal.split(",").forEach(function (str) {
                if (str.indexOf("@") > 0) {
                    datas.push({
                        id: str,
                        text: str
                    });
                }
            });
            $("#receiverId").select2('data', datas);
        });
    }
    if ($('#copyReceiverId').val()) {
        $.getJSON("http://127.0.0.1:9000/user/getByUserNames", {"userName": $('#copyReceiverId').val()}, function (jsonData) {
            if (jsonData.length <= 0) {
                return;
            }
            var datas = [];
            for (var i = 0; i < jsonData.length; i++) {
                datas.push({
                    id: jsonData[i].userName,
                    text: jsonData[i].userCnName
                });
            }
            //处理自己输入的邮箱
            var copyReceiverIdVal = $('#copyReceiverId').val();
            copyReceiverIdVal.split(",").forEach(function (str) {
                if (str.indexOf("@") > 0) {
                    datas.push({
                        id: str,
                        text: str
                    });
                }
            });
            $("#copyReceiverId").select2('data', datas);
        })
    }
    if ($('#smsReceiver').val()) {
        $.getJSON("http://127.0.0.1:9000/user/getByUserNames", {"userName": $('#smsReceiver').val()}, function (jsonData) {
            if (jsonData.length <= 0) {
                return;
            }
            var datas = [];
            for (var i = 0; i < jsonData.length; i++) {
                datas.push({
                    id: jsonData[i].userName,
                    text: jsonData[i].userCnName
                });
            }
            //处理自己输入的邮箱
            var smsReceiverVal = $('#smsReceiver').val();
            smsReceiverVal.split(",").forEach(function (str) {
                if (/^\d{5,21}$/.test(str)) {
                    datas.push({
                        id: str,
                        text: str
                    });
                }
            });
            $("#smsReceiver").select2('data', datas);
        })
    }
    if ($('#queryReceiverid').val()) {
        $.getJSON("http://127.0.0.1:9000/user/getByUserNames", {"userName": $('#queryReceiverid').val()}, function (jsonData) {
            if (jsonData.length <= 0) {
                return;
            }
            var datas = [];
            for (var i = 0; i < jsonData.length; i++) {
                datas.push({
                    id: jsonData[i].userName,
                    text: jsonData[i].userCnName
                });
            }
            $("#queryReceiverid").select2('data', datas);
        })
    }
    if ($('#queryCopyReceiverId').val()) {
        $.getJSON("http://127.0.0.1:9000/user/getByUserNames", {"userName": $('#queryCopyReceiverId').val()}, function (jsonData) {
            if (jsonData.length <= 0) {
                return;
            }
            var datas = [];
            for (var i = 0; i < jsonData.length; i++) {
                datas.push({
                    id: jsonData[i].userName,
                    text: jsonData[i].userCnName
                });
            }
            $("#queryCopyReceiverId").select2('data', datas);
        })
    }


    $("#mailTpl").bind('change', function () {
        var tplId = $('#mailTpl').val();
        if( tplId == 'unfinishedMail'){

        	$.ajax("http://nocworkstation.sysop.vipshop.com/notice/unfinishedDailyMailData", {
                dataType: "json",
                data: null,
                success: function (data) {
//                	填充主题
                	$('#emailTitle').val(data.emailTitle);
//                	填充发送人
                	var receiverString = data.receiver;
                	var receiverStringArray = receiverString.split(",");
                	var receiverIdString = data.receiverId;
                	var receiverIdStringArray = receiverIdString.split(",");
                	var datas = [];
                	for(var i = 0 ; i < receiverIdStringArray.length; i++){
                		datas.push({
                			id: receiverIdStringArray[i],
                			text: receiverStringArray[i]
                		});
                	}
//                	receiverString.split(",").forEach(function (str) {
//                        datas.push({
//                            id: str,
//                            text: str
//                        });
//                    });
                    $("#receiverId").select2('data', datas);

//                	设置内容
                	mailContentUm.execCommand('cleardoc');
                    mailContentUm.execCommand('inserthtml', data.content);
//                  填充附件
                    $('#attachmentList').append(
                            '<li file_id=' + data.attached + '>																																'
                            + '<input type="hidden" name="attachment" value="' + data.attached + '"> '
                            + '<a target="_blank" style="padding-left: 0px;margin-right: 20px; " class="green file" href="http://nocworkstation.sysop.vipshop.com/file/downLoadFile.do?id=' + data.attached + '">' + data.attachedName + '</a>   '
                            + '<a target="_blank" href="http://nocworkstation.sysop.vipshop.com/file/downLoadFile.do?id=' + data.attached + '"><i class="fa fa-file"></i> 下载</a>                                             '
                            + '<a onclick="removeAttach(this);" href="javascript:void(0);"><i class="fa fa-times red"></i> 删除</a>                                       '
                            + '</li>                                                                                                                              '
                    );
                }
            });
        }else{

        	var param = {eventId: $('#eventId').val()};
            $.ajax("http://nocworkstation.sysop.vipshop.com/notice/tpl/" + tplId, {
                dataType: "html",
                data: param,
                contentType: "application/x-www-form-urlencoded;charset=utf-8",
                success: function (data) {
                    mailContentUm.execCommand('cleardoc');
                    mailContentUm.execCommand('inserthtml', data);
                }
            });
        }

    })
    if ($("#mailTpl").val() != '') {
        $("#mailTpl").trigger('change');
    }


    $("#smsTpl").bind('change', function () {
        var tplId = $('#smsTpl').val();
        var param = {eventId: $('#eventId').val()};
        $.ajax("http://nocworkstation.sysop.vipshop.com/notice/tpl/" + tplId, {
            data: param,
            contentType: "application/x-www-form-urlencoded;charset=utf-8",
            success: function (data) {
                $("#smsContent").val(data);
            }
        });
    })
    if ($("#smsTpl").val() != '') {
        $("#smsTpl").trigger('change');
    }


    // 文件上传
    $('#uploadFileInput').bind('change', function () {
        uploadFile('http://nocworkstation.sysop.vipshop.com/file/uploadFile.do', 'uploadFileInput', function (list) {

            $.each(list, function () {
                $('#attachmentList').append(
                    '<li file_id=' + this.id + '>																																'
                    + '<input type="hidden" name="attachment" value="' + this.id + '"> '
                    + '<a target="_blank" style="padding-left: 0px;margin-right: 20px; " class="green file" href="http://nocworkstation.sysop.vipshop.com/file/downLoadFile.do?id=' + this.id + '">' + this.origin_file + '</a>   '
                    + '<a target="_blank" href="http://nocworkstation.sysop.vipshop.com/file/downLoadFile.do?id=' + this.id + '"><i class="fa fa-file"></i> 下载</a>                                             '
                    + '<a onclick="removeAttach(this);" href="javascript:void(0);"><i class="fa fa-times red"></i> 删除</a>                                       '
                    + '</li>                                                                                                                              '
                );
            });


        });
    });
    //上传文件
    function uploadFile(url, inputId, fn) {
        var flag = false;
        var upLoadFiles = document.getElementById(inputId).files;//上传文件input框
        var formdata = new FormData();
        for (var i = 0; i < upLoadFiles.length; i++) {
            if (upLoadFiles[i].size > 5000000) {
                alert('文件大小不能超过5000k！');
                flag = true;
                return;
            } else {
                formdata.append("uploadFiles_" + i, upLoadFiles[i]);
            }
        }
        if (flag) {
            return;
        }
        var xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
        xhr.send(formdata);
        xhr.onload = function (e) {
            if (xhr.status === 200) {
                var json = JSON.parse(xhr.responseText);
                if (json.success === false) {
                    alert(json.message);
                } else {
                    fn && fn(json.object);
                    //alert("上传成功");
                }
            }
        };
    }
});

function loadMailReceiver(selector, description) {
    $(selector).select2(
        {
            placeholder: description,
            allowClear: true,
            multiple: true,
            query: function (query) {
                var data = {
                    results: []
                };
                // $.getJSON("http://127.0.0.1:9000/user/query", {
                $.getJSON("http://192.168.98.145:9000/user/query", {
                    "userName": query.term
                }, function (jsonData) {
                    if (jsonData != '') {
                        $.each(jsonData, function (index, item) {
                            data.results.push({
                                id: item.userId,
                                text: item.userName
                                //如果读取来自nocworkstations的用户信息，启用以下字段
                                //id: item.userName,
                                //text: item.displayName
                            });
                        });
                    } else if (query.term.indexOf("@") > 0) {
                        data.results.push({
                            id: query.term,
                            text: query.term
                        });
                    }
                    query.callback(data);
                });
            }
        });
}


function loadSmsReceiver(selector, description) {
    $(selector).select2(
        {
            placeholder: description,
            allowClear: true,
            multiple: true,
            query: function (query) {
                var data = {
                    results: []
                };
                $.getJSON("http://127.0.0.1:9000/user/query", {
                    "userName": query.term
                }, function (jsonData) {
                    if (jsonData != '') {
                        $.each(jsonData, function (index, item) {
                            data.results.push({
                                id: item.userId,
                                text: item.userName
                                //如果读取来自nocworkstations的用户信息，启用以下字段
                                //id: item.userName,
                                //text: item.displayName
                            });
                        });
                    } else if (/^\d{5,21}$/.test(query.term)) {
                        data.results.push({
                            id: query.term,
                            text: query.term
                        });
                    }
                    query.callback(data);
                });
            }
        });
}


function goPage(page) {
    $("#page").val(page);
    $("#pageSize").val($("#txtPageSize").val());
    if($("#page").val() == '' || $("#pageSize").val() == '' || $("#pageSize").val() == 0){
    	alert("请输入正常的  页数 或者 每页显示条数");
    	return ;
    }
    $("#query-form").submit();
}

function chooseGroup(objId,groupType) {
    $('#chooseGroupModal').modal({
        backdrop: 'static'
    });
    $("#sourceid").val(objId);
    $("#groupType").val(groupType);
    queryEmailGroup(1);
}
function queryEmailGroup(pageIndex) {
    $.getJSON("http://nocworkstation.sysop.vipshop.com/notice/email/group/query", {
            'page': pageIndex,
            'groupName': $('#emailGroupName').val(),
            'groupType':$('#groupType').val()
        }, function (jsonData) {
            $("#emailGroupTable tbody").html("");
            $.each(jsonData.emailGroupList, function (index, value) {
                var recipients = value.recipients;
                if (recipients.length > 30) {
                    recipients = recipients.substring(0, 30) + "...";
                }
                var trHtml = "  <tr>" +
                    "<td><input type='checkbox' name='selectedGroup' value='" + value.groupId + "#" + value.emailGroupName + "'></td>" +
                    "<td>" + (index + 1) + "</td>" +
                    "<td>" + value.emailGroupName + "</td>" +
                    "<td><span data-placement='top' class='popovers' data-trigger='hover' data-content='" + value.recipients + "'>" +
                    recipients +
                    "</span></td>" +
                    "</tr>";
                $("#emailGroupTable tbody").append($(trHtml));
            });
            //分页
            if (jsonData.totalPage == 0) {
                jsonData.totalPage = 1;
            }
            var options = {
                bootstrapMajorVersion: 3,
                currentPage: jsonData.page,
                totalPages: jsonData.totalPage,
                size: "normal",
                alignment: "center",
                itemTexts: function (type, page, current) {
                    switch (type) {
                        case "first":
                            return "第一页";
                        case "prev":
                            return "<";
                        case "next":
                            return ">";
                        case "last":
                            return "最后页";
                        case "page":
                            return page;
                    }
                },
                onPageClicked: function (e, originalEvent, type, page) {
                    queryEmailGroup(page);
                }
            }


            $('#paginationDiv').bootstrapPaginator(options);
        }
    );


}
function okEmailGroup() {
    var selectedGroupVal = '';
    var groupNames = '';
    $("input[name='selectedGroup']").each(function (index, value) {
        if ($(value).is(':checked')) {
            selectedGroupVal += $(value).val().split("#")[0] + ",";
            groupNames += $(value).val().split("#")[1] + ",";
        }
    });
    if (groupNames != '' || selectedGroupVal != '') {
        selectedGroupVal = selectedGroupVal.substring(0, selectedGroupVal.length - 1);
        groupNames = groupNames.substring(0, groupNames.length - 1);
    }
    if (confirm("是否添加组：" + groupNames)) {
        var smsUrl = 'http://nocworkstation.sysop.vipshop.com/notice/email/group/getSms';
        var emailUrl = "http://nocworkstation.sysop.vipshop.com/notice/email/group/getEmail";
        var url;
        var sourceid = $("#sourceid").val();
        if (sourceid == 'copyReceiverId' || sourceid == 'receiverId') {
            url = emailUrl;
        } else {
            url = smsUrl;
        }
        $.ajax(url, {
            data: {'groupids': selectedGroupVal},
            dataType: 'json',
            success: function (data) {
                var selectData = $("#" + sourceid).select2('data');
                if (!selectData) {
                    selectData = [];
                }
                for (var prop in data) {
                    selectData.push({
                        id: data[prop],
                        text: prop
                    });
                }
                $("#" + sourceid).select2('data', selectData);

                $('#chooseGroupModal').modal('hide');
            }
        });
    }
}

function vilateForm(type) {
    var validate = false;
    var form;
    if (type == 'email') {
        form = $('#mailForm');
    } else {
        form = $('#smsForm');
    }
    var error2 = $('.alert-danger', form);
    var success2 = $('.alert-success', form);
    error2.hide();
    success2.hide();
    if (type == 'email') {
        var receiverIdVal = $('#receiverId').val();
        if (!receiverIdVal || receiverIdVal == '') {
            validate = false;
        } else {
            validate = true;
        }
    } else { //sms
        var smsReceiverVal = $('#smsReceiver').val();
        if (!smsReceiverVal || smsReceiverVal == '') {
            validate = false;
        } else {
            validate = true;
        }

    }
    if (!validate) {
        success2.hide();
        error2.show();
        return false;
    } else {
        error2.hide();
        success2.show();
        return true;
    }
}

function removeAttach(btn) {
    var fileNameStr = $(btn).parent().find("a").first().text();
    var file_id = $(btn).closest("li").attr("file_id");
    if (confirm('确认删除"' + fileNameStr + '"？')) {
        url = "http://nocworkstation.sysop.vipshop.com/file/deleteFile.do";
        param = {"id": file_id};
        $.post(url, param, function (data) {
            if (data.success) {
                $(btn).parent().remove();
            }
            else {
                alert(data.message);
            }
        });


    }
}