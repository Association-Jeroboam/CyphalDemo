# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/electricity/Source.0.1.dsdl
#
# Generated at:  2022-05-18 08:39:35.208817 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.electricity.Source
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.electricity
import uavcan.si.unit.energy


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Source_0_1:
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
                 power:       None | reg.udral.physics.electricity.Power_0_1 = None,
                 energy:      None | uavcan.si.unit.energy.Scalar_1_0 = None,
                 full_energy: None | uavcan.si.unit.energy.Scalar_1_0 = None) -> None:
        """
        reg.udral.physics.electricity.Source.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param power:       reg.udral.physics.electricity.Power.0.1 power
        :param energy:      uavcan.si.unit.energy.Scalar.1.0 energy
        :param full_energy: uavcan.si.unit.energy.Scalar.1.0 full_energy
        """
        self._power:       reg.udral.physics.electricity.Power_0_1
        self._energy:      uavcan.si.unit.energy.Scalar_1_0
        self._full_energy: uavcan.si.unit.energy.Scalar_1_0

        if power is None:
            self.power = reg.udral.physics.electricity.Power_0_1()
        elif isinstance(power, reg.udral.physics.electricity.Power_0_1):
            self.power = power
        else:
            raise ValueError(f'power: expected reg.udral.physics.electricity.Power_0_1 '
                             f'got {type(power).__name__}')

        if energy is None:
            self.energy = uavcan.si.unit.energy.Scalar_1_0()
        elif isinstance(energy, uavcan.si.unit.energy.Scalar_1_0):
            self.energy = energy
        else:
            raise ValueError(f'energy: expected uavcan.si.unit.energy.Scalar_1_0 '
                             f'got {type(energy).__name__}')

        if full_energy is None:
            self.full_energy = uavcan.si.unit.energy.Scalar_1_0()
        elif isinstance(full_energy, uavcan.si.unit.energy.Scalar_1_0):
            self.full_energy = full_energy
        else:
            raise ValueError(f'full_energy: expected uavcan.si.unit.energy.Scalar_1_0 '
                             f'got {type(full_energy).__name__}')

    @property
    def power(self) -> reg.udral.physics.electricity.Power_0_1:
        """
        reg.udral.physics.electricity.Power.0.1 power
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._power

    @power.setter
    def power(self, x: reg.udral.physics.electricity.Power_0_1) -> None:
        if isinstance(x, reg.udral.physics.electricity.Power_0_1):
            self._power = x
        else:
            raise ValueError(f'power: expected reg.udral.physics.electricity.Power_0_1 got {type(x).__name__}')

    @property
    def energy(self) -> uavcan.si.unit.energy.Scalar_1_0:
        """
        uavcan.si.unit.energy.Scalar.1.0 energy
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._energy

    @energy.setter
    def energy(self, x: uavcan.si.unit.energy.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.energy.Scalar_1_0):
            self._energy = x
        else:
            raise ValueError(f'energy: expected uavcan.si.unit.energy.Scalar_1_0 got {type(x).__name__}')

    @property
    def full_energy(self) -> uavcan.si.unit.energy.Scalar_1_0:
        """
        uavcan.si.unit.energy.Scalar.1.0 full_energy
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._full_energy

    @full_energy.setter
    def full_energy(self, x: uavcan.si.unit.energy.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.energy.Scalar_1_0):
            self._full_energy = x
        else:
            raise ValueError(f'full_energy: expected uavcan.si.unit.energy.Scalar_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.power._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.energy._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.full_energy._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 128 <= (_ser_.current_bit_length - _base_offset_) <= 128, \
            'Bad serialization of reg.udral.physics.electricity.Source.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Source_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "power"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.electricity.Power_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "energy"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.si.unit.energy.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f2_ holds the value of "full_energy"
        _des_.pad_to_alignment(8)
        _f2_ = uavcan.si.unit.energy.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = Source_0_1(
            power=_f0_,
            energy=_f1_,
            full_energy=_f2_)
        _des_.pad_to_alignment(8)
        assert 128 <= (_des_.consumed_bit_length - _base_offset_) <= 128, \
            'Bad deserialization of reg.udral.physics.electricity.Source.0.1'
        assert isinstance(self, Source_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'power=%s' % self.power,
            'energy=%s' % self.energy,
            'full_energy=%s' % self.full_energy,
        ])
        return f'reg.udral.physics.electricity.Source.0.1({_o_0_})'

    _EXTENT_BYTES_ = 16

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8$FPKA0{^{N-)|g89ltbj++0eVD!>Cj#0aWz24`)@PI{>*YU<#oa_d@kC_$*&&h5_KcgXI}vNL=3AtI$hphjBJpezz^m3ZI<'
        'A)a_cyzqz+{7HOfX7}#=D+N?x>3q90^Zot#e!g=L&;91rOC9%DeJ!8FI!=O6i$d~5{*(_A5rmOSbETybb@jPDQ<RY@3vqXni~32u'
        '^kMy=?o|t6##8LSRESYf#syD;oF-aEIuMD7Od%s_Cc&O6iwMV_4acI;Qe`!Ds>S!3=O^`cXZy@A>ksSdV#p1I2Bi_Yejf%-acz34'
        't`@eWNaC4G-7w~chsOFz&-g`JsJ`)Z4|mnRC~8`y3#~8o9PHDjM#1GdRaZ(rj(8Sm8I+kcQ$1l+7KO-6uov-!H`>l@cUo;TWv7Le'
        '7c!MbjuF;{tweEiINKM)fiz(vvXP;Bn<3PQYZIm_MyM}UU)*iQtyr*$y|?X_&F?SjckAl&p*B2=c@fVm`UrYbK0+jAYz+?!9vRd{'
        'qh4FhGjvqnT;Eu|*1xvCapT5%|N6Cl|N71T+S<#j8*BabjsC{<wHr6DUEkPPt*xzcfJB|=X)X%rJQv0)s;dr`d3AZN#^GS%5%i#@'
        'm+9*oA;uyvM8u7V>qph|;ZPokILuXHLK)XP)r+BaV8TWs!ki<3YSDfrascOd0oa3GyZQtPJF^1Yq%1<8$z@%2Hzzsq<hDpvU41z('
        '2MMYMV3diqHv<krKkthSK@Gukw$OET>1e6z>IGlyU@ce;Y)NZlGkrNEuHl_MV{1H?fd3=v(@o@JkU;;H76G$L;GjABURTe(F3nr+'
        'eGjh<7OJzM%Ik`qrbJKDfkJTb<ZT2CeAz0#gKBW2iW#ELhY?A154~5tu*>6EW}{<==tp*Ur%Vv$<mfImjCoRu`s2E{%^vFkdOY`v'
        '>g{LC0m4mXX2FUFeqbLKEntyxE8PvnLC!Nr13TqF4;*e5+w9teVdbPI{OXY=9IM3ek@)o9qbtqR(l(=SQ9vsn(JHO~5AZ%`Z8kn~'
        'dIb>v8I_v8^N3#Eq3_bI9=%SRbeq0MTl5Cqp*O3=#><+vElg;~L4w|)cb!l4eY!Wz`TNr+?l<E$#Wb{;r4jrmeB=XU+U|88Yq~#|'
        '#i=ppp|BqID4{P=MQM4Wo7Gt~11Qz;r0pxul;Gt#uB@x)9a{qMYct5ZSnl08)9KvaWU64dHd!Jw!CFC<TN(C~l4k}SC3L{v5E;Of'
        'B$H)kNU)(w615NDu%`S>%TdN6m5uQNgfO1x2_#?Xb{V_MY^z(cn;suRT(e=JQm5~TWnDsg!ZKm@RdJsg<qm;lW7ZSFC|G737BJ&1'
        'yq5xR<IUk=RjsttGihnGNQT~uh`oKzJWI8z2cSGrOqP74t;5igi4nI!1ofw(;NDy}eqmE(mLjtg+q$~oyBap^3_VfX508V$VTXP$'
        'v|W7-tFO&g+rx*K8=x)Zet7n)-``b+CroB`&KRE_w;6O#sg}%|LbUm6iY2rAKmy9J(<JD$DmQYCmJ>_e>a-`F()tum`O4A34t$O#'
        '|4&L;_^~Pzafnm?LVtcLr=0g*e%6#SU*M^U{ylcK)49bkAvLZV+Mp!_{-?kqQ@&Sts!EgzZ(a(E+%Tk-4FtnvPq<9mHkm7+%xojg'
        'THior(7j9Ok(5uYEG`Bji|r<;z)70MY(%^mi4_t&F~oX9(2s98kcDkIk-84S?RB}qWTEW!VVO~x${3us%!G;Nz~*M!)N&#0{R2(|'
        'WipFp<m}=q8%ynNTgHQbiEupCWTFsu@{1-9U=$aPQ*EiNPzNq?8XjY~hE2M@ZF{0;-3&c$W3#lx@}%^XBeJn9RF)zSuG5ClmPJs~'
        'CdH)_#_sU3<x;!W_M_A1DF`)lO*3;EuC=9%8HZEepOvdl3Z3`^5}8l6)q6b4F5;BS%$aTU+sK;wv=|ryA2GA|L06$ox$gGnGjP>^'
        'Ev>YMyIU~jV&nH+y=8)In8K0YGLtsjmXL9AWBc&D)V@@Oy-8{dm_umcY*28^F1A3xuqu|j#>Qr5<=ICY#@5-EpWC{(DV?Dl7|=3z'
        'S!)V?m|p&b2D&&Gp5@7ZeReIx@g+1(`O{jOAnh1gF&nuFiwL{OAZLEhS0kRzB!+T`;?Q8i%tcq&-vF$)r|vwph0r*TQJee4ALvE;'
        'JN=RVN&h(cjzPbokLfY}8aHPT)#KNQ>aVxF>&Q(Lm+~{g<>c^O?=^A2$+8%zX~@gR%j}vQfO<>qU(LD36p@L=FV1LcEAB5D4nTaY'
        'Bzhr{T-!5ZID}=S1Q=^B0QmidmIM<__6gG;zG<=a-^}t){ITDiHmCpdlfOM>NYmf^ME?M*9~__PN0ytz53&02_~FCLb~*(A29;;L'
        '$4C$W00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
