from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)


@app.route('/get_mszoning', methods=['GET'])
def get_mszoning():
    response = jsonify({
        'mszoning': util.get_mszoning()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


# @app.route('/get_lotshape', methods=['GET'])
# def get_lotshape():
#     response = jsonify({
#         'lotshape': util.get_lotshape()
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#
#     return response


# @app.route('/get_landcontour', methods=['GET'])
# def get_landcontour():
#     response = jsonify({
#         'landcontour': util.get_landcontour()
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#
#     return response


# @app.route('/get_utilities', methods=['GET'])
# def get_utilities():
#     response = jsonify({
#         'utilities': util.get_utilities()
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#
#     return response


# @app.route('/get_lotconfig', methods=['GET'])
# def get_lotconfig():
#     response = jsonify({
#         'lotconfig': util.get_lotconfig()
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#
#     return response


# @app.route('/get_landslope', methods=['GET'])
# def get_landslope():
#     response = jsonify({
#         'landslope': util.get_landslope()
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#
#     return response


@app.route('/get_neighbourhood', methods=['GET'])
def get_neighbourhood():
    response = jsonify({
        'neighbourhood': util.get_neighbourhood()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


# @app.route('/get_blgtyp', methods=['GET'])
# def get_blgtyp():
#     response = jsonify({
#         'blgtyp': util.get_blgtyp()
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#
#     return response


# @app.route('/get_hosestyle', methods=['GET'])
# def get_hosestyle():
#     response = jsonify({
#         'housestyle': util.get_hosestyle()
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#
#     return response


# @app.route('/get_exterior1', methods=['GET'])
# def get_exterior1():
#     response = jsonify({
#         'exterior1': util.get_exterior1()
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#
#     return response


# @app.route('/get_exterior2', methods=['GET'])
# def get_exterior2():
#     response = jsonify({
#         'exterior2': util.get_exterior1()
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#
#     return response


# @app.route('/get_msvnrtype', methods=['GET'])
# def get_msvnrtype():
#     response = jsonify({
#         'msvnrtype': util.get_msvnrtype()
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#
#     return response


# @app.route('/get_foundation', methods=['GET'])
# def get_foundation():
#     response = jsonify({
#         'foundation': util.get_foundation()
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#
#     return response

#
# @app.route('/get_electrical', methods=['GET'])
# def get_electrical():
#     response = jsonify({
#         'electrical': util.get_electrical()
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#
#     return response


@app.route('/get_garagetype', methods=['GET'])
def get_garagetype():
    response = jsonify({
        'garagetype': util.get_garagetype()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_garagefinish', methods=['GET'])
def get_garagefinish():
    response = jsonify({
        'garagefinish': util.get_garagefinish()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_paveddrive', methods=['GET'])
def get_paveddrive():
    response = jsonify({
        'paveddrive': util.get_paveddrive()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_saletype', methods=['GET'])
def get_saletype():
    response = jsonify({
        'saletype': util.get_saletype()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_salecondition', methods=['GET'])
def get_salecondition():
    response = jsonify({
        'salecondition': util.get_salecondition()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_remodelflag', methods=['GET'])
def get_remodelflag():
    response = jsonify({
        'remodelflag': util.get_remodelflag()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    lotfrontage = float(request.form['lotfrontage'])
    lotarea = float(request.form['lotarea'])
    street = int(request.form['street'])
    condition1 = int(request.form['condition1'])
    condition2 = int(request.form['condition2'])
    overallqual = float(request.form['overallqual'])
    overallcond = float(request.form['overallcond'])
    yearbuilt = float(request.form['yearbuilt'])
    yearremodadd = float(request.form['yearremodadd'])
    roofmatl = int(request.form['roofmatl'])
    masvnrarea = int(request.form['masvnrarea'])
    exterqual = float(request.form['exterqual'])
    extercond = float(request.form['extercond'])
    bsmtqual = float(request.form['bsmtqual'])
    bsmtcond = float(request.form['bsmtcond'])
    bsmtexposure = float(request.form['bsmtexposure'])
    bsmtfintype1 = float(request.form['bsmtfintype1'])
    bsmtfinsf1 = float(request.form['bsmtfinsf1'])
    bsmtfintype2 = float(request.form['bsmtfintype2'])
    bsmtfinsf2 = int(request.form['bsmtfinsf2'])
    bsmtunfsf = float(request.form['bsmtunfsf'])
    totalbsmtsf = float(request.form['totalbsmtsf'])
    heating = int(request.form['heating'])
    heatingqc = float(request.form['heatingqc'])
    centralair = int(request.form['centralair'])
    firstflrsf = float(request.form['firstflrsf'])
    secondflrsf = int(request.form['secondflrsf'])
    lowqualfinsf = int(request.form['lowqualfinsf'])
    grlivarea = float(request.form['grlivarea'])
    bsmtfullbath = float(request.form['bsmtfullbath'])
    bsmthalfbath = int(request.form['bsmthalfbath'])
    fullbath = float(request.form['fullbath'])
    halfbath = int(request.form['halfbath'])
    bedroomabvgr = float(request.form['bedroomabvgr'])
    kitchenabvgr = float(request.form['kitchenabvgr'])
    kitchenqual = float(request.form['kitchenqual'])
    totrmsabvgrd = float(request.form['totrmsabvgrd'])
    functional = int(request.form['functional'])
    fireplaces = float(request.form['fireplaces']) ##---> switched from into to float
    fireplacequ = float(request.form['fireplacequ']) ##----> switched from into to float
    garagecars = float(request.form['garagecars'])
    garagearea = float(request.form['garagearea'])
    garagequal = float(request.form['garagequal'])
    garagecond = float(request.form['garagecond'])
    wooddecksf = float(request.form['wooddecksf'])
    openporchsf = int(request.form['openporchsf'])
    enclosedporch = int(request.form['enclosedporch'])
    threessnporch = int(request.form['threessnporch'])
    screenporch = int(request.form['screenporch'])
    poolarea = int(request.form['poolarea'])
    miscval = int(request.form['miscval'])
    mosold = float(request.form['mosold'])
    yrsold = int(request.form['yrsold'])

    exterqualscore = float(request.form['exterqualscore'])
    bsmtqualscore = float(request.form['bsmtqualscore'])
    garagequalscore = float(request.form['garagequalscore'])
    overallqualscore = float(request.form['overallqualscore'])
    age_house = float(request.form['age_house'])
    ##
    overallqualsq = float(request.form['overallqualsq'])
    grlivareasq = float(request.form['grlivareasq'])
    garagecarssq = float(request.form['garagecarssq'])
    garageareasq = float(request.form['garageareasq'])
    totalbsmtsfsq = float(request.form['totalbsmtsfsq'])
    firstflrsfsq = float(request.form['firstflrsfsq'])
    fullbathsq = float(request.form['fullbathsq'])
    totrmsabvgrdsq = float(request.form['totrmsabvgrdsq'])
    yearbuiltsq = float(request.form['yearbuiltsq'])

    msZoning = request.form['msZoning']
    lotShape = request.form['lotShape']
    landContour = request.form['landContour']
    utilities = request.form['utilities']
    lotConfig = request.form['lotConfig']
    landSlope = request.form['landSlope']
    neighbourhood = request.form['neighbourhood']
    blgType = request.form['blgType']
    houseStyle = request.form['houseStyle']
    exterior1 = request.form['exterior1']
    exterior2 = request.form['exterior2']
    msvnrtype = request.form['msvnrtype']
    foundation = request.form['foundation']
    electrical = request.form['electrical']
    garageType = request.form['garageType']
    garageFinish = request.form['garageFinish']
    pavedDrive = request.form['pavedDrive']
    saleType = request.form['saleType']
    saleCondition = request.form['saleCondition']
    remodelFlag = request.form['remodelFlag']

    response = jsonify({
        'estimated_price': util.get_estimated_price(lotfrontage, lotarea, street, condition1, condition2, overallqual,
                                                    overallcond, yearbuilt, yearremodadd, roofmatl, masvnrarea,
                                                    exterqual,
                                                    extercond, bsmtqual, bsmtcond, bsmtexposure, bsmtfintype1,
                                                    bsmtfinsf1,
                                                    bsmtfintype2, bsmtfinsf2, bsmtunfsf, totalbsmtsf, heating,
                                                    heatingqc,
                                                    centralair, firstflrsf, secondflrsf, lowqualfinsf, grlivarea,
                                                    bsmtfullbath,
                                                    bsmthalfbath, fullbath, halfbath, bedroomabvgr, kitchenabvgr,
                                                    kitchenqual,
                                                    totrmsabvgrd, functional, fireplaces, fireplacequ, garagecars,
                                                    garagearea,
                                                    garagequal, garagecond, wooddecksf, openporchsf, enclosedporch,
                                                    threessnporch,
                                                    screenporch, poolarea, miscval, mosold, yrsold, exterqualscore,
                                                    bsmtqualscore,
                                                    garagequalscore, overallqualscore, age_house, overallqualsq,
                                                    grlivareasq,
                                                    garagecarssq, garageareasq, totalbsmtsfsq, firstflrsfsq, fullbathsq,
                                                    totrmsabvgrdsq, yearbuiltsq, msZoning, lotShape,
                                                    landContour, utilities, lotConfig, landSlope, neighbourhood,
                                                    blgType, houseStyle,
                                                    exterior1, exterior2, msvnrtype, foundation, electrical, garageType,
                                                    garageFinish,
                                                    pavedDrive, saleType, saleCondition, remodelFlag)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
