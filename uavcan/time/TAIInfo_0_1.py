# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/time/TAIInfo.0.1.dsdl
#
# Generated at:  2022-05-06 20:35:08.951224 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.time.TAIInfo
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class TAIInfo_0_1:
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
    DIFFERENCE_TAI_MINUS_GPS:         int = 19
    DIFFERENCE_TAI_MINUS_UTC_UNKNOWN: int = 0

    def __init__(self,
                 difference_tai_minus_utc: None | int | _np_.uint16 = None) -> None:
        """
        uavcan.time.TAIInfo.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param difference_tai_minus_utc: saturated uint10 difference_tai_minus_utc
        """
        self._difference_tai_minus_utc: int

        self.difference_tai_minus_utc = difference_tai_minus_utc if difference_tai_minus_utc is not None else 0  # type: ignore

    @property
    def difference_tai_minus_utc(self) -> int:
        """
        saturated uint10 difference_tai_minus_utc
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._difference_tai_minus_utc

    @difference_tai_minus_utc.setter
    def difference_tai_minus_utc(self, x: int | _np_.uint16) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 1023:
            self._difference_tai_minus_utc = x
        else:
            raise ValueError(f'difference_tai_minus_utc: value {x} is not in [0, 1023]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(max(min(self.difference_tai_minus_utc, 1023), 0), 10)
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of uavcan.time.TAIInfo.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> TAIInfo_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "difference_tai_minus_utc"
        _f0_ = _des_.fetch_aligned_unsigned(10)
        self = TAIInfo_0_1(
            difference_tai_minus_utc=_f0_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of uavcan.time.TAIInfo.0.1'
        assert isinstance(self, TAIInfo_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'difference_tai_minus_utc=%s' % self.difference_tai_minus_utc,
        ])
        return f'uavcan.time.TAIInfo.0.1({_o_0_})'

    _EXTENT_BYTES_ = 2

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8e1>&m0{@j)ZEqAe5Dt`=aL^VMg!-ZugW3v|%jRAn$$|QTCZtL)goq>ssX{C7uJ7!!XRmB;l0#G~A6gY@rB=fIG5y$I)4$Of'
        '@4aj&Y1R93d*k)Y<MGV%%>8)k_dhSp_)l>)8zv@6gU~Q7Xeyr5C}lwyt3jrWu*?<j?pU42HrH%-m@)U--F)eOa5sw6p`-&?pUdff'
        'Ol4rjfCanvHa28WxneflXW9rQ9iJ)Aemi=8?YcAF6F<9`t~ei3Yqf}S%Zz&p{*FO1dCL{2*9A+HDS}#<P)kFLu#VfFX)zF1>?6=U'
        'X+&SLWJ6lkXZq-I&WDk(VajCRa@Vba^OzbN4phP%zg%3|9y`Kq!78jhz$HA<PwtT`E{DcanNXcn9lgpUe!BP|5xpMMOvWs<RD=T|'
        'a}(w^cEzbMQL%gS*QuGAUCv0HYk19)=>`%pd%&0^kXix($lmU1oroTJCe?uq$VQLk(m&UUVU}1$o-?h2T5XpLL-uK!Gcuq<5_2m1'
        'i~vf=_{6K<>HUtpkOMAKMl8o&#xhO7i_WDKvR|(yEMqc(N1`MV)({$rRM;VgRS}#`60M@#*fOvoJ*@_W9fBW8Q({!EV`h#8XAcCN'
        'n35r*x=x@1jfm1=1(F#8q(KGJUBa!+%$>zWCW8a<Ok^w(G*G&~h`$y$8O@+1VkMKHwj(g1=tnC^15_kYJ#wFF%h6@RVwN%u3vg6;'
        '?Fd380Z7D%Zwn}cfUGGZl_j}hMCI0qgq5z~bn8kJ%|<s^CmbFy07mZRX-ZN78G_Infa!!Kc)1I3vDJGo6IjP@kq~PAZfr8#c%TKM'
        'yi=<Y_^iQ|;x~EmHb>u;$A5~iE=)cz7XIzy-F`zQX?B)d;I`Q)EqOYzG^_8l(bB3~ZlR@JwcJL_t*T`SEw`(dWwb0+Eh}hQu39>1'
        'S*ci78ffWM5Uw=A(yC%!LCmdY)q<E?t*QkPwyKy{FnX(sxr4D<Rm>e9YpLR=<6|vXEk4#t)q?qHb*g?a8|^CQ4rZfW&2tCO-k#>U'
        ')oA!#?W)DUb8F(K)o3D~_U)<#PugCp>}vX0%eC4)gZ0&Fv>NqMy(0Ca4S%K3PNb|SPa3|LSX%bdm{YL+a1j|xvjLET0d|R*Mt%q!'
        'P~v;V?5dJTn0CUze2!lkJ$=}n<sb1+`PE-a`dr&sU%&t8{?_XK5PXIYHn#S5!mqb?9KTllF)454&z?AhZkiT9Fr^&fg;si#O2LKi'
        'DC}k6D(vPF5iw9N;0w<-*tfLo^YI2kf%&E#P7GIhnh*#B`)v6>Fe1i@hJ+@bF+HJ7p#`ou6Z$51#V2F&VuzV#2DS2tbj?2U8K&tt'
        'TYSDa*V8mctAX|P(KD<UCz~CIl4K&t-e+$~ZmmpisZHdq$%QKn_qMuQ4<Bz~l4l?w4@QxByExI9L}0~SMajcxSdIl4iSSGOCjXq@'
        '<;ywfD`*Gs9Z*%`UKQ_!{;I-EX&Z{fZ55ZoQXOC+Wno4^J&UvWm5Rs}=eB`&54X|!8r1s4B1k7!IDeeXgez*R!;I5(jSXP-_&Cd>'
        'RK%fX{XE5Z(>Vchb*7wGU_aiZD=v;^mY@+d1H1)iQP1Z>P7T07ImVe{AC$?x;@6(YlPJ}AmEe?kr=T1?A>lh76}9o@1rp_pWh8}J'
        '*#N#2l<yoIL_inIt0niW8i<(e!j?LrsZnEbHdshdjg0+=*d6f~mi|KY=LL7#sfLSe(hOc!xMnDG--B*>$Yxae3kw*#j)h+zPakN6'
        ';{&XoN>g=Uyb58hf9V@!9*An(bCU(!H%~VGYGblmd+eq0`sU8{u|AF`Aej#$7(Re^Dx72P{2#d=6$PPL2IWwmeB7#D&LJNt>>lC)'
        'XA-*}`nsR02)0!cf#4)#pwvNa!U142Rx8;DCy6jIR4?rV`}Dl{Q-jd}KGp=tJ+wS9L9Ah>nUH`TO%uu&#W?4f<|^a>r^G0Q(*0sg'
        '6VnM34r|~1?TQOu3A^ck@30BO7Vm^Aa|Johi5U(e1yP~)A3z_$1dZVzW;hWkJ)M-#gfYxxiQ`X;_qR)K`^QT>!qqL9b*LV`xyt8%'
        'bvL@T-%JF56SC5S>(1s8oD)W4*S&}j^bjA;;sg#|jQDFvk5u}95?gtM>=XPARz0s<%nSek'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
