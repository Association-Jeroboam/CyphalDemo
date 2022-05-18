# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/dynamics/translation/Linear.0.1.dsdl
#
# Generated at:  2022-05-18 08:39:34.080988 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.dynamics.translation.Linear
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.kinematics.translation
import uavcan.si.unit.force


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Linear_0_1:
    """
    Generated property settings use relaxed type signatures, accepting a large variety of
    possible representations of the value, which are automatically converted to a well-defined
    internal representation. When accessing a property, this strict well-defined internal
    representation is always returned. The implicit strictification enables more precise static
    type analysis.

    The value returned by the __repr__() method may be invariant to some of the field values,
    and its format is not guaranteed to be stable. Therefore, the returned string representation
    can be used only for displaying purposes; any kind of automation build on top of that will
    be fragile and prone to mismaintenance.
    """
    def __init__(self,
                 kinematics: None | reg.udral.physics.kinematics.translation.Linear_0_1 = None,
                 force:      None | uavcan.si.unit.force.Scalar_1_0 = None) -> None:
        """
        reg.udral.physics.dynamics.translation.Linear.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param kinematics: reg.udral.physics.kinematics.translation.Linear.0.1 kinematics
        :param force:      uavcan.si.unit.force.Scalar.1.0 force
        """
        self._kinematics: reg.udral.physics.kinematics.translation.Linear_0_1
        self._force:      uavcan.si.unit.force.Scalar_1_0

        if kinematics is None:
            self.kinematics = reg.udral.physics.kinematics.translation.Linear_0_1()
        elif isinstance(kinematics, reg.udral.physics.kinematics.translation.Linear_0_1):
            self.kinematics = kinematics
        else:
            raise ValueError(f'kinematics: expected reg.udral.physics.kinematics.translation.Linear_0_1 '
                             f'got {type(kinematics).__name__}')

        if force is None:
            self.force = uavcan.si.unit.force.Scalar_1_0()
        elif isinstance(force, uavcan.si.unit.force.Scalar_1_0):
            self.force = force
        else:
            raise ValueError(f'force: expected uavcan.si.unit.force.Scalar_1_0 '
                             f'got {type(force).__name__}')

    @property
    def kinematics(self) -> reg.udral.physics.kinematics.translation.Linear_0_1:
        """
        reg.udral.physics.kinematics.translation.Linear.0.1 kinematics
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._kinematics

    @kinematics.setter
    def kinematics(self, x: reg.udral.physics.kinematics.translation.Linear_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.translation.Linear_0_1):
            self._kinematics = x
        else:
            raise ValueError(f'kinematics: expected reg.udral.physics.kinematics.translation.Linear_0_1 got {type(x).__name__}')

    @property
    def force(self) -> uavcan.si.unit.force.Scalar_1_0:
        """
        uavcan.si.unit.force.Scalar.1.0 force
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._force

    @force.setter
    def force(self, x: uavcan.si.unit.force.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.force.Scalar_1_0):
            self._force = x
        else:
            raise ValueError(f'force: expected uavcan.si.unit.force.Scalar_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.kinematics._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.force._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 128 <= (_ser_.current_bit_length - _base_offset_) <= 128, \
            'Bad serialization of reg.udral.physics.dynamics.translation.Linear.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Linear_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "kinematics"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.kinematics.translation.Linear_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "force"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.si.unit.force.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = Linear_0_1(
            kinematics=_f0_,
            force=_f1_)
        _des_.pad_to_alignment(8)
        assert 128 <= (_des_.consumed_bit_length - _base_offset_) <= 128, \
            'Bad deserialization of reg.udral.physics.dynamics.translation.Linear.0.1'
        assert isinstance(self, Linear_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'kinematics=%s' % self.kinematics,
            'force=%s' % self.force,
        ])
        return f'reg.udral.physics.dynamics.translation.Linear.0.1({_o_0_})'

    _EXTENT_BYTES_ = 16

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8$FPKA0{^{MTWcgm6i#+?PuvUf0!Fl1WX%fOxlOVYQCT-@RAw_9HoC0H(p%kKGp9&*SJPEJ$%qSCMA=}0LdqxKd=wRZ(kH<m'
        'p-<wQZ$A11Jk>p&nM^VX3cG<J)u*b?<vZUwr*;Ou{A0W?`%^E(O<(wd?FgDM60i@68&KQvco=iRB-QGP4Vk2#OcVNUGp2e^UwWYL'
        '>uELUL?p!h%L%R9sh^O*j-e@-Cv3loTV^2>5{ZCF#v}U%izrF78gUvl5h&5nr-pC0)_c0rSLy#$KhSF2AyOvHO(hljE?Vm0<NhhF'
        '23Hvk{I+jnj!z_Uq;VKd<w6)#GlyN>M6W`0@MvdY7)A@fU;=%Cb1h|)9crITNy8(NEts7~OxgjB>Jsb?j|7E|{z_k=qphM>U~$4i'
        'CRqam8(j@Jkq3bvcU&f&+=#AN7_3KxbVBZ9urI2o*Nf}sn!SR1Yi7$J{E5D$)sv2pB=Sk(cPe^_dO}i1|5M)>t|i1XPzcP}YHN);'
        ')JqGc+4=JPLTPDfp}aU>E-x;Z=jN`=mgdR}rE+O;ZfSXbu~eGX##ZVgJcA*X6caz-_}tT~52Zv+b|l$xn>m;6Yq$az1V-r7IH4Yq'
        ')YrS}j8kLV)OTW@NQe2ls?Ixtr-?^#BcM)9(0?^-{sqiM-`A14+v`TUhj{hRpl#rWtEXb7)!0fi1`=GSA=hduPThcc4l*MRjJ-B<'
        'F!G^1vv^V9#Q~FD6t)mkXY&l(bM~xl@~EYOchUhO(5Hk((j>OQJgRr049kds8=%&UMcUi&<3ZW|t<}UeCU0cl8~E8GfI98)SSzcS'
        '644A@jv=8ZYZxMu%B1dQOcNq`(x%an;{n5>f!pfrI`MrL)ejwl56o^g4KU1R_bzH^kRYY{b3I+Lz7Q^!cAP8Hm66oNa6=XuhT?*3'
        'o5iqUDdKEyk2!QZ#)>n%s-~`RGqQ|iZ71svh!~2FD!Avn3a&u|?lIXsx#ZwtYjvq&!OLL7%tM%kh5y0oa~Z20!~|jYc;vSnCh!W<'
        '_#;RKyt)goRpE7bV;Zi(3S5UbVHMtjx8WT%Qn;+4Vps#!j3ICnZe<R_dvIqz1$XyXB;WK4#Gz(@hB^iV_+z-Y*@0!-NN+4JbYV$6'
        'j|L{urVTzuJg2(x>;>&tppS)iqBDX=32&F7%tdNkoQ43Nh0h>_Z$PC-`l?Q2!@;?g4I|UL@^OS!(H=-R2|Gp-wwrt?VY8WQx0@_7'
        '^~@S?&=4DrMFJkxEfQH|n+aQ=6!D#oI)7?~N2cXQM>Y&Kn)eHAYi1~)pzW93=&!v_zTX2{_?QYKy^7MSZE111OZ;_y_#R5{9X@<e'
        '+)7#}zQ<I>R998hI8K|#Sq?)H-IDvX%9;Nc{CO<%2Qx1pCFKhXWp$=XsurtRX|x&ftw`@v|2H@f|G@7@(;mKs@8EkiQalhf`~W|;'
        'Y5eng*8CgP%IsK7SRTLZGkgl*WVW`L1S>9%6oX=>=yEd$TG!Zm!W+!TYbN8EZwp^N_}H*Q(!?qW_?9JsqW(yvAx$jFEj*l}RgWf;'
        'un2?qeHs<lMCyS>M0P18LRh?(t?_;4|Cc&DsWN`*!C&}0C;JXccMg;NpxC6#{ufD60W#+c000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
