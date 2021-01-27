import pickle
import json
import numpy as np

_model = None
_data_columns = None
_msZoning = None
_lotShape = None
_landContour = None
_utilities = None
_lotConfig = None
_landSlope = None
_neighbourhood = None
_blgType = None
_houseStyle = None
_exterior1 = None
_exterior2 = None
_msvnrtype = None
_foundation = None
_electrical = None
_garageType = None
_garageFinish = None
_pavedDrive = None
_saleType = None
_saleCondition = None
_remodelFlag = None


def load_saved_artifacts():
    global _model
    global _data_columns
    global _msZoning
    global _lotShape
    global _landContour
    global _utilities
    global _lotConfig
    global _landSlope
    global _neighbourhood
    global _blgType
    global _houseStyle
    global _exterior1
    global _exterior2
    global _msvnrtype
    global _foundation
    global _electrical
    global _garageType
    global _garageFinish
    global _pavedDrive
    global _saleType
    global _saleCondition
    global _remodelFlag

    if _model is None:
        with open('./artifacts/ames_home_prices_model.pickle', 'rb') as f:
            _model = pickle.load(f)
    print("loading model....")

    with open('./artifacts/columns.json', 'r') as f:
        _data_columns = json.load(f)['data_columns']
        _msZoning = _data_columns[67:72]  # Identifies the general zoning classification of the sale
        # _street = _data_columns[62:64]  # Type of road access to property
        _lotShape = _data_columns[72:76]  # General shape of property
        _landContour = _data_columns[76:80]  # Flatness of the property
        _utilities = _data_columns[80:82]  # Type of utilities available
        _lotConfig = _data_columns[82:87]  # Lot configuration (inside lot, corner lot)
        _landSlope = _data_columns[87:90]  # Slope of property
        _neighbourhood = _data_columns[90:115]
        # _condition1 = _data_columns[107:116]  # Proximity to various conditions
        # _condition2 = _data_columns[116:124]
        _blgType = _data_columns[115:120]  # Type of dwelling
        _houseStyle = _data_columns[120:128]  # Style of dwelling
        # _roofMat = _data_columns[137:144]  # Roof material
        _exterior1 = _data_columns[128:143]
        _exterior2 = _data_columns[143:159]
        _msvnrtype = _data_columns[159:163]  # Masonry veneer type
        _foundation = _data_columns[163:169]
        # _heating = _data_columns[169:175]
        # _centrailAir = _data_columns[175:177]
        _electrical = _data_columns[169:173]  # Electrical system
        _garageType = _data_columns[173:180]
        _garageFinish = _data_columns[180:184]
        _pavedDrive = _data_columns[184:187]
        _saleType = _data_columns[187:196]
        _saleCondition = _data_columns[196:202]
        _remodelFlag = _data_columns[202:208]


def get_estimated_price(lotfrontage, lotarea, street, condition1, condition2, overallqual,
                        overallcond, yearbuilt, yearremodadd, roofmatl, masvnrarea, exterqual,
                        extercond, bsmtqual, bsmtcond, bsmtexposure, bsmtfintype1, bsmtfinsf1,
                        bsmtfintype2, bsmtfinsf2, bsmtunfsf, totalbsmtsf, heating, heatingqc,
                        centralair, firstflrsf, secondflrsf, lowqualfinsf, grlivarea, bsmtfullbath,
                        bsmthalfbath, fullbath, halfbath, bedroomabvgr, kitchenabvgr, kitchenqual,
                        totrmsabvgrd, functional, fireplaces, fireplacequ, garagecars, garagearea,
                        garagequal, garagecond, wooddecksf, openporchsf, enclosedporch, threessnporch,
                        screenporch, poolarea, miscval, mosold, yrsold, exterqualscore, bsmtqualscore,
                        garagequalscore, overallqualscore, age_house, overallqualsq, grlivareasq,
                        garagecarssq, garageareasq, totalbsmtsfsq, firstflrsfsq, fullbathsq,
                        totrmsabvgrdsq, yearbuiltsq, msZoning, lotShape,
                        landContour, utilities, lotConfig, landSlope, neighbourhood, blgType, houseStyle,
                        exterior1, exterior2, msvnrtype, foundation, electrical, garageType, garageFinish,
                        pavedDrive, saleType, saleCondition, remodelFlag):
    try:
        msZoning_index = _data_columns.index(msZoning.lower())
    except:
        msZoning_index = -1

    try:
        lotShape_index = _data_columns.index(lotShape.lower())
    except:
        lotShape_index = -1

    try:
        landContour_index = _data_columns.index(landContour.lower())
    except:
        landContour_index = -1

    try:
        utilities_index = _data_columns.index(utilities.lower())
    except:
        utilities_index = -1

    try:
        lotConfig_index = _data_columns.index(lotConfig.lower())
    except:
        lotConfig_index = -1

    try:
        landSlope_index = _data_columns.index(landSlope.lower())
    except:
        landSlope_index = -1

    try:
        neighbourhood_index = _data_columns.index(neighbourhood.lower())
    except:
        neighbourhood_index = -1

    try:
        blgType_index = _data_columns.index(blgType.lower())
    except:
        blgType_index = -1

    try:
        houseStyle_index = _data_columns.index(houseStyle.lower())
    except:
        houseStyle_index = -1

    try:
        exterior1_index = _data_columns.index(exterior1.lower())
    except:
        exterior1_index = -1

    try:
        exterior2_index = _data_columns.index(exterior2.lower())
    except:
        exterior2_index = -1

    try:
        msvnrtype_index = _data_columns.index(msvnrtype.lower())
    except:
        msvnrtype_index = -1

    try:
        foundation_index = _data_columns.index(foundation.lower())
    except:
        foundation_index = -1

    try:
        electrical_index = _data_columns.index(electrical.lower())
    except:
        electrical_index = -1

    try:
        garageType_index = _data_columns.index(garageType.lower())
    except:
        garageType_index = -1

    try:
        garageFinish_index = _data_columns.index(garageFinish.lower())
    except:
        garageFinish_index = -1

    try:
        pavedDrive_index = _data_columns.index(pavedDrive.lower())
    except:
        pavedDrive_index = -1

    try:
        saleType_index = _data_columns.index(saleType.lower())
    except:
        saleType_index = -1

    try:
        saleCondition_index = _data_columns.index(saleCondition.lower())
    except:
        saleCondition_index = -1

    try:
        remodelFlag_index = _data_columns.index(remodelFlag.lower())
    except:
        remodelFlag_index = -1

    x = np.zeros(len(_data_columns))

    x[0] = lotfrontage
    x[1] = lotarea
    x[2] = street
    x[3] = condition1
    x[4] = condition2
    x[5] = overallqual
    x[6] = overallcond
    x[7] = yearbuilt
    x[8] = yearremodadd
    x[9] = roofmatl
    x[10] = masvnrarea
    x[11] = exterqual
    x[12] = extercond
    x[13] = bsmtqual
    x[14] = bsmtcond
    x[15] = bsmtexposure
    x[16] = bsmtfintype1
    x[17] = bsmtfinsf1
    x[18] = bsmtfintype2
    x[19] = bsmtfinsf2
    x[20] = bsmtunfsf
    x[21] = totalbsmtsf
    x[22] = heating
    x[23] = heatingqc
    x[24] = centralair
    x[25] = firstflrsf
    x[26] = secondflrsf
    x[27] = lowqualfinsf
    x[28] = grlivarea
    x[29] = bsmtfullbath
    x[30] = bsmthalfbath
    x[31] = fullbath
    x[32] = halfbath
    x[33] = bedroomabvgr
    x[34] = kitchenabvgr
    x[35] = kitchenqual
    x[36] = totrmsabvgrd
    x[37] = functional
    x[38] = fireplaces
    x[39] = fireplacequ
    x[40] = garagecars
    x[41] = garagearea
    x[42] = garagequal
    x[43] = garagecond
    x[44] = wooddecksf
    x[45] = openporchsf
    x[46] = enclosedporch
    x[47] = threessnporch
    x[48] = screenporch
    x[49] = poolarea
    x[50] = miscval
    x[51] = mosold
    x[52] = yrsold
    ##
    x[53] = exterqualscore  ##
    x[54] = bsmtqualscore  ##
    x[55] = garagequalscore  ##
    x[56] = overallqualscore  ##
    x[57] = age_house  ##
    ##
    # x[58] = overallqualscore ** 2
    # x[59] = grlivarea ** 2
    # x[60] = garagecars ** 2
    # x[61] = garagearea ** 2
    # x[62] = totalbsmtsf ** 2
    # x[63] = firstflrsf ** 2
    # x[64] = fullbath ** 2
    # x[65] = totrmsabvgrd ** 2
    # x[66] = yearbuilt ** 2
    x[58] = overallqualsq
    x[59] = grlivareasq
    x[60] = garagecarssq
    x[61] = garageareasq
    x[62] = totalbsmtsfsq
    x[63] = firstflrsfsq
    x[64] = fullbathsq
    x[65] = totrmsabvgrdsq
    x[66] = yearbuiltsq

    if msZoning_index > 0:
        x[msZoning_index] = 1

    if lotShape_index > 0:
        x[lotShape_index] = 1

    if landContour_index > 0:
        x[landContour_index] = 1

    if utilities_index > 0:
        x[utilities_index] = 1

    if lotConfig_index > 0:
        x[lotConfig_index] = 1

    if landSlope_index > 0:
        x[landSlope_index] = 1

    if neighbourhood_index > 0:
        x[neighbourhood_index] = 1

    if blgType_index > 0:
        x[blgType_index] = 1

    if houseStyle_index > 0:
        x[houseStyle_index] = 1

    if exterior1_index > 0:
        x[exterior1_index] = 1

    if exterior2_index > 0:
        x[exterior2_index] = 1

    if msvnrtype_index > 0:
        x[msvnrtype_index] = 1

    if foundation_index > 0:
        x[foundation_index] = 1

    if electrical_index > 0:
        x[electrical_index] = 1

    if garageType_index > 0:
        x[garageType_index] = 1

    if garageFinish_index > 0:
        x[garageFinish_index] = 1

    if pavedDrive_index > 0:
        x[pavedDrive_index] = 1

    if saleType_index > 0:
        x[saleType_index] = 1

    if saleCondition_index > 0:
        x[saleCondition_index] = 1

    if remodelFlag_index > 0:
        x[remodelFlag_index] = 1

    return round(_model.predict([x])[0], 2)



def get_mszoning():
    return _msZoning

def get_lotshape():
    return _lotShape

def get_landcontour():
    return _landContour

def get_utilities():
    return _utilities

def get_lotconfig():
    return _lotConfig

def get_landslope():
    return _landSlope

def get_neighbourhood():
    return _neighbourhood

def get_blgtyp():
    return _blgType

def get_hosestyle():
    return _houseStyle

def get_exterior1():
    return _exterior1

def get_exterior2():
    return _exterior2

def get_msvnrtype():
    return _msvnrtype

def get_foundation():
    return _foundation

def get_electrical():
    return _electrical

def get_garagetype():
    return _garageType

def get_garagefinish():
    return _garageFinish

def get_paveddrive():
    return _pavedDrive

def get_saletype():
    return _saleType

def get_salecondition():
    return _saleCondition

def get_remodelflag():
    return _remodelFlag


if __name__ == '__main__':
    load_saved_artifacts()
    # print(get_saletype())
    x = get_estimated_price(0.16780822, 0.0331861, 1, 1, 1,
     0.44444444, 0.625, 0.61594203, 0.11666667, 1,
     0, 0.33333333, 0.75, 0.6, 0.75,
     0.25, 0.5, 0.16335932, 0.16666667, 0,
     0.16780822, 0.21505728, 1, 0.5, 1,
     0.2248738, 0, 0, 0.18462698, 0.33333333,
     0, 0.33333333, 0, 0.375, 0.33333333,
     0.33333333, 0.25, 1, 0, 0,
     0.25, 0.20733427, 0.6, 0.6, 0.29171529,
     0, 0, 0, 0, 0,
     0, 0.45454545, 1, 0.40909091, 0.45,
     0.36, 0.3258427, 0.38970588, 0.24242424, 0.05091453,
     0.0625, 0.0429875, 0.04624964, 0.07373498, 0.11111111,
     0.109375, 0.60753272, 'mszoning_rl', 'lotshape_reg', 'landcontour_lvl',
     'utilities_allpub', 'lotconfig_inside', 'landslope_gtl', 'neighborhood_names',
     'bldgtype_1fam', 'housestyle_1story', 'exterior1st_metalsd', 'exterior2nd_metalsd',
     'masvnrtype_none', 'foundation_cblock', 'electrical_sbrkr', 'garagetype_attchd',
     'garagefinish_rfn', 'paveddrive_y', 'saletype_wd', 'salecondition_normal', 'remod_flag_no')

    # print(x)
    # print(get_mszoning())

