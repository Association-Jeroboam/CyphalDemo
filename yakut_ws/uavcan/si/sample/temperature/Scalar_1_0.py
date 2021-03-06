# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/sample/temperature/Scalar.1.0.dsdl
#
# Generated at:  2022-05-18 08:59:57.533565 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.temperature.Scalar
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.time


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Scalar_1_0:
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
                 timestamp: None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 kelvin:    None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.temperature.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param kelvin:    saturated float32 kelvin
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._kelvin:    float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.kelvin = kelvin if kelvin is not None else 0.0  # type: ignore

    @property
    def timestamp(self) -> uavcan.time.SynchronizedTimestamp_1_0:
        """
        uavcan.time.SynchronizedTimestamp.1.0 timestamp
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, x: uavcan.time.SynchronizedTimestamp_1_0) -> None:
        if isinstance(x, uavcan.time.SynchronizedTimestamp_1_0):
            self._timestamp = x
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 got {type(x).__name__}')

    @property
    def kelvin(self) -> float:
        """
        saturated float32 kelvin
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._kelvin

    @kelvin.setter
    def kelvin(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._kelvin = x
        else:
            raise ValueError(f'kelvin: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.kelvin):
            if self.kelvin > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.kelvin < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.kelvin)
        else:
            _ser_.add_aligned_f32(self.kelvin)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.temperature.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "kelvin"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            kelvin=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.temperature.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'kelvin=%s' % self.kelvin,
        ])
        return f'uavcan.si.sample.temperature.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8jkSbg0{?Ya>uw#l5td}@?rUT_j-A+al3G%0ZFD>GaoV(X<r+>IpBS;-3cYy2-K7o*?X4tN(g{$Y`O(4#7U%+IfjmMUA&(HC'
        'Mbe)^pCITH<Y#Agxkr*?3y{89ayT=bEA`jo|Gau~r2Z+d=7UH_vFB^9B#Y&zEQq=1hgp(mS{iQ4lMjt5LQ^RIXpnRJ+%A4*|6&))'
        'aX)1V?7vg6-H@f8mY!xw4yO%Ia;_L2@g9aOX3CaR{w`NqW~mh;<>YT2{oK+~I`Vh>nJs61W{i?SVYs$`0{O47Y{+HH@w<}8(Sb!X'
        'e#8v(4Vo#&nnf{QUULQ-nSecmG!!aJ<)=J)1Pj`L%~ni`>DCf)0<?=W?)coR?8uc&q>;N|$K2yo%YMqE4^zYYTpjh(tRG0@$2{#D'
        'VQCkv44F25l0{(Uo8^TEtsp$+ZNlDt+(Os<&3<Cbb3WLZModMA1wAVQxY}$YLzQVBW@%*0<9?KdcI$s*BO{LlCuxxcT#;;>9OBZ%'
        '2xf?2yPV`qYaS6T(~uLLC7dt?Dil)#lE7zbh)jXM<}}_63U%usG*hw<+Y8d;-i?|I9ZUkI`67{;M0{I<PY9&K63g>ghRi_BJ%VDw'
        'LMfCpJc61E&1WD`B;Z8xKNk=iIKHj2<UqO}hOZVz5-^Ob8$@$nGldz*)j3>LrhQmdyAtkJn<8uNGjIzqZkNRcM=MQ6Qof6Bf<N1F'
        'w%6D<-0y5GflJ7qjKEGFGO+RenHfTs$m)~M#!=4#I}5VHkk!?0hYUDV`Ucq(G8DK4m64i(M{bji^;+hkvtV}txueKlR>Tn~0u6)|'
        'Y05*cHB&MkG$ueI5NY(#T5ua218XrN9nfk-R%qm^)x&mFfC$1s8wlq668x1K$YT;JsipRs%WTGw3o=~Vyxk)UX=cdXJBtJ|Aq8J5'
        '&=)cVNm1nJubU(oK#`)xoDJfP)iH)ZK|Anj!ymPwA_<z`2WBl;9Aktr-TE<Ks@WSA+x);$35SIyN6jz}kQDO<(*k{<a5sg(5OAXQ'
        'EEK}2a%wY6u}sXc?!=t9;;3u1E8Z6G(h;mDG2fKV<l`Rgef+zg6^rHd-*c6{sJhNKh#PuiC(ZU!&z2K@ZICVBYMTPz&mrNknH^~f'
        'Q=ioN$>P=?(J80l$|0_5*uU#&*e^$yEn237BH-oRp+4vbgQm&iEf&Nju_l%ZXebc}rBF^hvd_v>{<hrbk&l7$Wn_EhSzl*`3OQ`V'
        '+|L=bi*gbnmVqs&A3$T@e}Jpcp*@Yh2aQ8y*vZFoY0H_-K@PFH!;{RGm-8Zk!u1vJ7cuHP=&*2!iKel_dGwVnue`LmdMn<tht9GF'
        '+u58im<FS;{C!uT_8A1>U%jT_Q3F8@m@QEMnSySBPR6{2qGnLAW-n7aOLax)Lptl2)k+~#j5tzZARvp2rU%q5;6M+22-z1<W8l>+'
        'fd&^j#h9-_29lsVwOzQb!Cm0V)RNA5D7WRIJcj|X!#(W9K@2Xs-sZ_c>xN647r$+J;#bmqRDVC@!z3<``B`pD@+u*EkOUdT2fTV8'
        ';^ms+$Mx{d)WHav@IwLRZ^a+W(+^mLz3~T3g5hqjh+$k0UfdO(f7k`ut#kl`JZ~geI#mR4&qSs;)_`F9NKE2rgKR;ebQI5xRCLVY'
        'F~qTo9(Uj4h@%yqaO;z9eahjqTc1IksOYTYKY=(^(UXYBD|*WDpGKUm=oz<v7ID0yuQ@q$h_6-j9O9XZo<}@Y(F=$tD*8I&Ohqrc'
        '^KUr4mz<u<PR^T7-&=^6D|!X-Qbn&KzEM$vc(J0_5MQt8+lUt``VQjxioT0@uA)CeoU7<{XV*O9*@`YW`xX&TSM<lu&YvKjtmqAA'
        '?~=Q(=j?tDak`?*&i)m|$%?MJd#pKsth@WvaXnVi4R^1b&c9uEzgtb*>H7|U>hNa{KXCYShre+6ONaLyZaEYV_Z>cU__@O`9DeEW'
        'D~I1Y{LbO`4c?y`b;QM%SZIlEOWbRTt(FiivELF;TjKMU_@X7gY>BU0;@g(^t|h*AL;<fmm<TXOu(i9j02@0@oN06L-drq4aBvM@'
        'neY&tz6+z&9C<s!<RUP+R>k~N5S*|+JYoubHhxgfudOeyc30QdH#XL~oz-r)bE~_ua&viorMtG?UGJ=H+*<9duQ!vWRzI=B<6Wp#'
        'u_(TQK_hOXg0IC{@n7+uLTo-0cY5O2;@*PzQ2a(v@sYSMdgYjgkucG`>*0-l=w)xq)6LudXnz+EpP>TrSZp<&;}7D=u)%~w>dB#|'
        'a~@_l4zu*7-K(5#nitFq{I}qx(tNQ)N8yq&4Eh9qQ_%bG9xU_^buR+li)&=s0;a74rX6f#KUl_~dH)Ce>dezB4FCW'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
