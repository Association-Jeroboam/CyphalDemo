# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/file/Error.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.581920 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.file.Error
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_


def _restore_constant(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Error_1_0:
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
    OK:             int = 0
    UNKNOWN_ERROR:  int = 65535
    NOT_FOUND:      int = 2
    IO_ERROR:       int = 5
    ACCESS_DENIED:  int = 13
    IS_DIRECTORY:   int = 21
    INVALID_VALUE:  int = 22
    FILE_TOO_LARGE: int = 27
    OUT_OF_SPACE:   int = 28
    NOT_SUPPORTED:  int = 38

    def __init__(self,
                 value: None | int | _np_.uint16 = None) -> None:
        """
        uavcan.file.Error.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint16 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated uint16 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint16) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 65535:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 65535]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_u16(max(min(self.value, 65535), 0))
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of uavcan.file.Error.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Error_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_u16()
        self = Error_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of uavcan.file.Error.1.0'
        assert isinstance(self, Error_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.file.Error.1.0({_o_0_})'

    _EXTENT_BYTES_ = 2

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{@j&U2hyU6iwQ0vPqkeC{-mu&;e1@Mlfj-rA53z*blU9I<wl3(msIYnQ``7njMd9&$5dIqDY`tvIJ7huR!93KgjiF'
        '^U*XB+I`sZ_}b^5>p4F6mm7cmy*M}dnY;NoQAz3(#U!UG|B*&1^GPfQxlmj)YgRg17O^fQ>yC3~kL-gN_9uJalt@Mg7+){wFs7M*'
        '$Z=y$N+GQ&lOdCei_F5DS$sMjAKB)7bMANh!kU|eYAtzGXr}CUh;{{!(^b}#>YSy?S^i~`P)&(;q^{bYOFrP54{^mtFH^jqv80h{'
        ')@SndVs4U%Ym&08ufaCg5Im+zlYvN>h1=#%>jcPc^D7v8;zC%_+;6sR&26GI%@Qh;^FS|)2uh|jq-lW+ZjeO8*34O)T{Y#3$lM-%'
        'N&+_E&UEy4a}C~s_u=j_!nLqz;RE>4ERZSIdnfg>Q7)Ns$NO5f<u=tgN7EB@*fdLrlE!XUVZ1&aW8BO?w5|vhVX}|@kIPCgXa?c8'
        '0jagyVS7RgHsRB064)`NM|*p_dov&|1!0%e!(LFm1Z{q22BdN$ypq=ZER<IEE0tQOL#nl)QM-)Rwe8&*;BGY#s?n}hx?%e{qM0um'
        'KJ!2EP~B{hYnFJD(PZlfi5JcjnMb{xYVb5r?d5`JT6tRFY{DgrwUA?bfz8hLEX6f~r~3zuD#8C=&Cz*W^ZQ80-C)mMYL6=~6WT+u'
        '@x(h65~(mxQ`u+wc$FF}r2YntSw7Zky>U<@-7q8v`|Yo5mmTuX<5><l>~%?4C!N-Q<#M#oW;rA$%1*D<3ftYw6|j2-$IQk#KO@oj'
        '*cu(I2kY<v?!o8q2&(WU1n><!gDynyJq&=u2sHc(KZAjn1-eke@H)p7C1GEgRdUEjEFrm&n()L1W}PTe$e0oL5r`9sHH+?%^2nN{'
        '7FzbG<z|o2)8@C(b3izcUeNfYc<-<GxwdAxGR}dfRW=aTyqgzM%3~r~zeru?Ghf9G3&-w`NG_!{s}qO!xBZ8{Ga##-`)v@Q3h79e'
        'Y3IO09y9w2g|!th<>c+a{N*-NMXEh<h*CbMB2VN@PVCBeCK;ue_Tv+OJ9AS6))(Kcx%Cy-2b1>>JGD}Corv5T?<x>A9z+6bM&?iO'
        '46s|c?BRq4wy)E!us~wq*mK|?^Hz%{3D5d(EP{VsG$_)P%JIc0Z2n>IH`o4D5w^tq7{NBnMTB(@c;-3{4(P}Y7G1Z&FW~quJ71^S'
        'q-zF6<TU302Z7um-L?k+00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)