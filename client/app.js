function getBedroomAbvGr(){
    var uiBedroomAbvGr = document.getElementsByName("uiBedroomAbvGr");
    for(var i in uiBedroomAbvGr) {
        if(uiBedroomAbvGr[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1; // Invalid Value
}

function getTotRmsAbvGrd() {
  var uiTotRmsAbvGrd = document.getElementsByName("uiTotRmsAbvGrd");
  for(var i in uiTotRmsAbvGrd) {
    if(uiTotRmsAbvGrd[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getExterQual() {
  var uiExterQual = document.getElementsByName("uiExterQual");
  for(var i in uiExterQual) {
    if(uiExterQual[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getBasementQuality() {
  var uiBasementQuality = document.getElementsByName("uiBasementQuality");
  for(var i in uiBasementQuality) {
    if(uiBasementQuality[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getBasementCondition() {
  var uiBasementCondition = document.getElementsByName("uiBasementCondition");
  for(var i in uiBasementCondition) {
    if(uiBasementCondition[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getBasementExposure() {
  var uiBasementExposure = document.getElementsByName("uiBasementExposure");
  for(var i in uiBasementExposure) {
    if(uiBasementExposure[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getBsmtFinType1() {
  var uiBsmtFinType1 = document.getElementsByName("uiBsmtFinType1");
  for(var i in uiBsmtFinType1) {
    if(uiBsmtFinType1[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getKitchenQual() {
  var uiKitchenQual = document.getElementsByName("uiKitchenQual");
  for(var i in uiKitchenQual) {
    if(uiKitchenQual[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getGarageCars() {
  var uiGarageCars = document.getElementsByName("uiGarageCars");
  for(var i in uiGarageCars) {
    if(uiGarageCars[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getHeatingQC() {
  var uiHeatingQC = document.getElementsByName("uiHeatingQC");
  for(var i in uiHeatingQC) {
    if(uiHeatingQC[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getFireplaces() {
  var uiFireplaces = document.getElementsByName("uiFireplaces");
  for(var i in uiFireplaces) {
    if(uiFireplaces[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getFireplaceQu() {
  var uiFireplaceQu = document.getElementsByName("uiFireplaceQu");
  for(var i in uiFireplaceQu) {
    if(uiFireplaceQu[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getOverallQual() {
  var uiOverallQual = document.getElementsByName("uiOverallQual");
  for(var i in uiOverallQual) {
    if(uiOverallQual[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getOverallCondition() {
  var uiOverallCondition = document.getElementsByName("uiOverallCondition");
  for(var i in uiOverallCondition) {
    if(uiOverallCondition[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getUtility(){
 var uiUtility = document.getElementsByName("uiUtility");
   for(var i in uiUtility) {
    if(uiUtility[i].checked) {
        return uiUtility[i].value;
    }
  }
  return -1; // Invalid Value
}


function scalar(x, min, max){
    return (x-min)/(max-min)
}


function onClickedEstimatePrice() {
//
//   var lotfrontage = float(68.26)//log of LotFrontage -> normal dist


   var lotarea = document.getElementById("uiLotArea");//Lot area -> normal dist


//   var street = int(1)
//   var condition1 = int(1)
//   var condition2 = int(1)

    var overallqual = getOverallQual() //document.getElementById("uiOverallQual") --------------------> NOT REQUIRED


//    var overallcond = getOverallCondition() //document.getElementById("uiOverallCondition")
//    var yearbuilt = document.getElementById("uiYearBuilt")
//    var yearremodadd = int(1950) // we have a remodel flag as well // placeholding value
//    var roofmatl = int(1)
//    var masvnrarea = float(103.11) // normal dist
//    var exterqual = document.getElementById("uiExterQual")
//    var extercond = float(3) // have to scale (float) type
//    var bsmtqual = getBasementQuality() //document.getElementById("uiBasementQuality")
//    var bsmtcond = getBasementCondition() //document.getElementById("uiBasementCondition")
//    var bsmtexposure = getBasementExposure() //document.getElementById("uiBasementExposure")
//    var bsmtfintype1 = getBsmtFinType1() //document.getElementById("uiBsmtFinType1")
//    var bsmtfinsf1 = float(443.63) // (after log transform take mean)
//    var bsmtfintype2 = float(1.24) // (after log transform take mean)
//    var bsmtfinsf2 = int(46) // (after log transform take mean)
//    var bsmtunfsf = float(567.24) // (after log transform take mean)

    var totalbsmtsf = document.getElementById("uiTotalBsmtSF")

//    var heating = int(1)
//    var heatingqc = getHeatingQC() //document.getElementById("uiHeatingQC")
//    var centralair = int(1)
//    var firstflrsf = float(1162.62) // not sure but try to prefill
//    var secondflrsf = int(0)
//    var lowqualfinsf = int(0)
//    var grlivarea = float(1515.4) /////--------
//    var bsmtfullbath = 1.0 // take i/p float
//    var bsmthalfbath = 1
//    var fullbath = 1.0 // recheck
//    var halfbath = 1
//    var bedroomabvgr = getBedroomAbvGr() //document.getElementById("uiBedroomAbvGr")
//    var kitchenabvgr = int(1)// have to scale (float) type
//    var kitchenqual = getKitchenQual() //document.getElementById("uiKitchenQual")
//    var totrmsabvgrd = getTotRmsAbvGrd() //document.getElementById("uiTotRmsAbvGrd")
//    var functional = int(1)
//    var fireplaces = getFireplaces() //document.getElementById("uiFireplaces")
//    var fireplacequ = getFireplaceQu() //document.getElementById("uiFireplaceQu")
//    var garagecars = getGarageCars() //document.getElementById("uiGarageCars")
//    var garagearea = float(472.98) //log in perfect normal
//    var garagequal = float(request.form['garagequal'])// have to scale (float) type
//    var garagecond = float(request.form['garagecond'])// have to scale (float) type
//    var wooddecksf = float(94.244) // log in perfect normal
//    var openporchsf = int(46.66) // log in perfect normal
//    var enclosedporch = int(21.95) // log in perfect normal
//    var threessnporch = int(3) // log in perfect normal
//    var screenporch = int(15) // log in perfect normal

    var poolarea = document.getElementById("uiPoolArea")


//    var miscval = int(0)
//    var mosold = document.getElementById("uiMoSold")
//    var yrsold = document.getElementById("uiYrSold")
//
//    var exterqualscore = float(exterqual*extercond)
//    var bsmtqualscore = float(bsmtqual*bsmtcond)
//    var garagequalscore = float(garagequal*garagecond)
//    var overallqualscore = float(overallqual*overallcond)
//    var age_house = float(10)
//    //
//    var overallqualsq = float(overallqual ** 2)
//    var grlivareasq = float(grlivarea ** 2)
//    var garagecarssq = float(garagecars ** 2)
//    var garageareasq = float(garagearea ** 2)
//    var totalbsmtsfsq = float(totalbsmtsf ** 2)
//    var firstflrsfsq = float(firstflrsf ** 2)
//    var fullbathsq = float(fullbath ** 2)
//    var totrmsabvgrdsq = float(totrmsabvgr ** 2)
//    var yearbuiltsq = float(yearbuilt ** 2)


    var msZoning = document.getElementById("uiMsZoning")
    var lotShape = document.getElementById("uiLotShape")


//    var landContour = "landcontour_bnk"
//    var utilities = document.getElementById("uiUtility") //--
//    var lotConfig = "lotconfig_corner"
//    var landSlope = "landslope_mod"

    var neighbourhood = document.getElementById("uiNeighbourhood")


//    var blgType = "bldgtype_1fam"


    var houseStyle = document.getElementById("uiHouseStyle")
    var exterior1 = document.getElementById("uiExterior1st")
//

//    var exterior2 = "exterior2nd_asphshn"


    var msvnrtype = document.getElementById("uiMasVnrType")
    var foundation = document.getElementById("uiFoundation")


//    var electrical = "electrical_fusef"


    var garageType = document.getElementById("uiGarageType")
    var garageFinish = document.getElementById("uiGarageFinish")


//    var pavedDrive = "paveddrive_p"
//    var saleType = "saletype_conld"
//    var saleCondition = "salecondition_adjland"


    var remodelFlag = document.getElementById("uiremod_flag")

   var estPrice = document.getElementById("uiEstimatedPrice");


   var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
//  var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
    lotfrontage: parseFloat(0.16788),     //log of LotFrontage -> normal dist
    lotarea: scalar(lotarea.value, 1300, 215245),  //0.03318      //Lot area -> normal dist
    street: parseInt(1),
    condition1: parseInt(1),
    condition2: parseInt(1),
    overallqual: scalar(getOverallQual(), 1, 10), // 0.4444
    overallcond: scalar(getOverallCondition(), 1, 10), // 0.625
    yearbuilt: parseFloat(0.6159), // 0.6159
    yearremodadd: parseFloat(0.1166), // we have a remodel flag as well // placeholding value
    roofmatl: parseInt(1),
    masvnrarea: parseInt(0), // normal dist
    exterqual: scalar(getExterQual(), 1, 10),
    extercond: parseFloat(0.75), // have to scale (float) type
    bsmtqual: scalar(getBasementQuality(), 1, 10), //0.6
    bsmtcond: scalar(getBasementCondition(), 1, 10), // 0.75
    bsmtexposure: scalar(getBasementExposure(), 1, 10), // 0.25
    bsmtfintype1: scalar(getBsmtFinType1(), 1, 10), // 0.5
    bsmtfinsf1: parseFloat(0.1633), // (after log transform take mean)
    bsmtfintype2: parseFloat(0.1666), // (after log transform take mean)
    bsmtfinsf2: parseInt(0), // (after log transform take mean)
    bsmtunfsf: parseFloat(0.1678), // (after log transform take mean)
    totalbsmtsf: scalar(totalbsmtsf.value, 0, 6110), // 0.2150-------------------------------------------------------
    heating: parseInt(1),
    heatingqc: scalar(getHeatingQC(), 1, 5), // 0.5
    centralair: parseInt(1),
    firstflrsf: parseFloat(0.2248) ,// not sure but try to prefill
    secondflrsf: parseInt(0),
    lowqualfinsf: parseInt(0),
    grlivarea: parseFloat(0.184), /////--------
    bsmtfullbath: parseFloat(0.333), // take i/p float
    bsmthalfbath: parseInt(0),
    fullbath: parseFloat(0.333), // recheck
    halfbath: parseInt(1),
    bedroomabvgr: parseFloat(0.375), // 0.375
    kitchenabvgr: parseFloat(0.333),// have to scale (float) type
    kitchenqual: scalar(getKitchenQual(), 1, 10), // 0.333
    totrmsabvgrd: parseFloat(0.25), // 0.25
    functional: parseInt(1),
    fireplaces: scalar(getFireplaces(), 0, 3), // 0
    fireplacequ: scalar(getFireplaceQu(), 0, 5), // 0
    garagecars: scalar(getGarageCars(), 0, 4), // 0.25
    garagearea: parseFloat(0.207), //log in perfect normal
    garagequal: parseFloat(0.6),// have to scale (float) type
    garagecond: parseFloat(0.6),// have to scale (float) type
    wooddecksf: parseFloat(0.291), // log in perfect normal
    openporchsf: parseInt(0), // log in perfect normal
    enclosedporch: parseFloat(0), // log in perfect normal
    threessnporch: parseInt(0), // log in perfect normal
    screenporch: parseInt(0), // log in perfect normal
    poolarea: scalar(poolarea.value, 0, 738), // 0
    miscval: parseInt(0),
    mosold: parseFloat(0.4545), // 0.4545
    yrsold: parseInt(1), // 1
    exterqualscore: scalar(getExterQual(), 1, 10)*parseFloat(0.75),
    bsmtqualscore: scalar(getBasementQuality(), 1, 10)*scalar(getBasementCondition(), 1, 10),
    garagequalscore: parseFloat(0.36),
    overallqualscore:  scalar(getOverallQual(), 1, 10)*scalar(getOverallCondition(), 1, 10),
    age_house: parseFloat(0.389),
    overallqualsq: scalar(getOverallQual(), 1, 10)*scalar(getOverallCondition(), 1, 10)**2,
    grlivareasq: parseFloat(0.05091),
    garagecarssq: scalar(getGarageCars(), 0, 4)**2,
    garageareasq: parseFloat(0.04298),
    totalbsmtsfsq: scalar(totalbsmtsf.value, 0, 6110)**2,
    firstflrsfsq: parseFloat(0.07373),
    fullbathsq: parseFloat(0.1111),
    totrmsabvgrdsq: parseFloat(0.109375),
    yearbuiltsq: parseFloat(0.60753),
    msZoning: msZoning.value, // "mszoning_rl"//'residential low density',
    lotShape: lotShape.value,//"reg", 'regular'// ui
    landContour: "lvl", // Lvl
    utilities: getUtility(),//"utilities_allpub", //--
    lotConfig: "inside", //Inside
    landSlope: "gtl", //Gtl
    neighbourhood: neighbourhood.value, //"neighborhood_names",'names'
    blgType: "1fam",//1Fam
    houseStyle: houseStyle.value,//  "one story"//ui
    exterior1: exterior1.value,//"metalsd",'metal siding',//ui
    exterior2: "metal siding",
    msvnrtype: msvnrtype.value,//"none", // ui
    foundation: foundation.value,//"cblock",'cinder block',//ui
    electrical: "sbrkr",//SBrkr
    garageType: 'attached to home',//garageType.value,
    garageFinish: 'rough finished',//garageFinish.value,
    pavedDrive: "y",//y
    saleType: "wd", //wd
    saleCondition: "normal",//normal
    remodelFlag: remodelFlag.value//"no"//ui
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " $ </h2>";
      console.log(status);
  });
}



function onPageLoad() {
  console.log( "document loaded" );
//   var url1 = "http://127.0.0.1:5000/get_mszoning";// Use this if you are NOT using nginx which is first 7 tutorials
    var url1 = "/api/get_mszoning"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

//    var url2 = "http://127.0.0.1:5000/get_neighbourhood";
    var url2 = "/api/get_neighbourhood";

    var url3 = "/api/get_garagetype";
//    var url3 = "http://127.0.0.1:5000/get_garagetype";

    var url4 = "/api/get_garagefinish";
//    var url4 = "http://127.0.0.1:5000/get_garagefinish";

    var url5 = "/api/get_lotshape";
//    var url5 = "http://127.0.0.1:5000/get_lotshape";

    var url6 = "/api/get_housestyle";
//    var url6 = "http://127.0.0.1:5000/get_hosestyle";

    var url7 = "/api/get_exterior1";
//    var url7 = "http://127.0.0.1:5000/get_exterior1";

    var url8 = "/api/get_msvnrtype";
//    var url8 = "http://127.0.0.1:5000/get_msvnrtype";

    var url9 = "/api/get_foundation";
//    var url9 = "http://127.0.0.1:5000/get_foundation";

    var url10 = "/api/get_remodelflag";
//    var url10 = "http://127.0.0.1:5000/get_remodelflag";



  $.get(url1,function(data, status) {
      console.log("got response for get_get_mszoning request");
      if(data) {
          var mszoning = data.mszoning;
          var uiMsZoning = document.getElementById("uiMsZoning");
          $('#uiMsZoning').empty();
          for(var i in mszoning) {
              var opt = new Option(mszoning[i]);
              $('#uiMsZoning').append(opt);
          }
      }
  });

  $.get(url2,function(data, status) {
      console.log("got response for get_uiNeighbourhood request");
      if(data) {
          var neighbourhood = data.neighbourhood;
          var uiNeighbourhood = document.getElementById("uiNeighbourhood");
          $('#uiNeighbourhood').empty();
          for(var i in neighbourhood) {
              var opt = new Option(neighbourhood[i]);
              $('#uiNeighbourhood').append(opt);
          }
      }
  });

  $.get(url3,function(data, status) {
      console.log("got response for get_garagetype request");
      if(data) {
          var garagetype = data.garagetype;
          var uiGarageType = document.getElementById("uiGarageType");
          $('#uiGarageType').empty();
          for(var i in garagetype) {
              var opt = new Option(garagetype[i]);
              $('#uiGarageType').append(opt);
          }
      }
  });

  $.get(url4,function(data, status) {
      console.log("got response for get_garagefinish request");
      if(data) {
          var garagefinish = data.garagefinish;
          var uiGarageFinish = document.getElementById("uiGarageFinish");
          $('#uiGarageFinish').empty();
          for(var i in garagefinish) {
              var opt = new Option(garagefinish[i]);
              $('#uiGarageFinish').append(opt);
          }
      }
  });

  $.get(url5,function(data, status) {
      console.log("got response for get_lotShape request");
      if(data) {
          var lotShape = data.lotshape;
          var uiLotShape = document.getElementById("uiLotShape");
          $('#uiLotShape').empty();
          for(var i in lotShape) {
              var opt = new Option(lotShape[i]);
              $('#uiLotShape').append(opt);
          }
      }
  });

    $.get(url6,function(data, status) {
      console.log("got response for get_houseStyle request");
      if(data) {
          var housestyle = data.housestyle;
          var uiHouseStyle = document.getElementById("uiHouseStyle");
          $('#uiHouseStyle').empty();
          for(var i in housestyle) {
              var opt = new Option(housestyle[i]);
              $('#uiHouseStyle').append(opt);
          }
      }
  });

    $.get(url7,function(data, status) {
      console.log("got response for get_exterior1 request");
      if(data) {
          var exterior1 = data.exterior1;
          var uiExterior1st = document.getElementById("uiExterior1st");
          $('#uiExterior1st').empty();
          for(var i in exterior1) {
              var opt = new Option(exterior1[i]);
              $('#uiExterior1st').append(opt);
          }
      }
  });

    $.get(url8,function(data, status) {
      console.log("got response for get_msvnrtype request");
      if(data) {
          var msvnrtype = data.msvnrtype;
          var uiMasVnrType = document.getElementById("uiMasVnrType");
          $('#uiMasVnrType').empty();
          for(var i in msvnrtype) {
              var opt = new Option(msvnrtype[i]);
              $('#uiMasVnrType').append(opt);
          }
      }
  });

    $.get(url9,function(data, status) {
      console.log("got response for get_foundation request");
      if(data) {
          var foundation = data.foundation;
          var uiFoundation = document.getElementById("uiFoundation");
          $('#uiFoundation').empty();
          for(var i in foundation) {
              var opt = new Option(foundation[i]);
              $('#uiFoundation').append(opt);
          }
      }
  });

    $.get(url10,function(data, status) {
      console.log("got response for get_remodelFlag request");
      if(data) {
          var remodelflag = data.remodelflag;
          var uiremod_flag = document.getElementById("uiremod_flag");
          $('#uiremod_flag').empty();
          for(var i in remodelflag) {
              var opt = new Option(remodelflag[i]);
              $('#uiremod_flag').append(opt);
          }
      }
  });


    var coll = document.getElementsByClassName("collapsible");
    var i;

    for (i = 0; i < coll.length; i++) {
      coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
          content.style.display = "none";
        } else {
          content.style.display = "block";
        }
      });
    }

}

window.onload = onPageLoad;

