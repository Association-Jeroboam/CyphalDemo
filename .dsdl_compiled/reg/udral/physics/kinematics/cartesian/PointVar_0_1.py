# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/cartesian/PointVar.0.1.dsdl
#
# Generated at:  2022-05-06 20:25:55.317916 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.cartesian.PointVar
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.kinematics.cartesian


def _restore_constant(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class PointVar_0_1:
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
                 value:          None | reg.udral.physics.kinematics.cartesian.Point_0_1 = None,
                 covariance_urt: None | _NDArray_[_np_.float16] | list[float] = None) -> None:
        """
        reg.udral.physics.kinematics.cartesian.PointVar.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value:          reg.udral.physics.kinematics.cartesian.Point.0.1 value
        :param covariance_urt: saturated float16[6] covariance_urt
        """
        self._value:          reg.udral.physics.kinematics.cartesian.Point_0_1
        self._covariance_urt: _NDArray_[_np_.float16]

        if value is None:
            self.value = reg.udral.physics.kinematics.cartesian.Point_0_1()
        elif isinstance(value, reg.udral.physics.kinematics.cartesian.Point_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.cartesian.Point_0_1 '
                             f'got {type(value).__name__}')

        if covariance_urt is None:
            self.covariance_urt = _np_.zeros(6, _np_.float16)
        else:
            if isinstance(covariance_urt, _np_.ndarray) and covariance_urt.dtype == _np_.float16 and covariance_urt.ndim == 1 and covariance_urt.size == 6:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._covariance_urt = covariance_urt
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                covariance_urt = _np_.array(covariance_urt, _np_.float16).flatten()
                if not covariance_urt.size == 6:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'covariance_urt: invalid array length: not {covariance_urt.size} == 6')
                self._covariance_urt = covariance_urt
            assert isinstance(self._covariance_urt, _np_.ndarray)
            assert self._covariance_urt.dtype == _np_.float16  # type: ignore
            assert self._covariance_urt.ndim == 1
            assert len(self._covariance_urt) == 6

    @property
    def value(self) -> reg.udral.physics.kinematics.cartesian.Point_0_1:
        """
        reg.udral.physics.kinematics.cartesian.Point.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.kinematics.cartesian.Point_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.cartesian.Point_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.cartesian.Point_0_1 got {type(x).__name__}')

    @property
    def covariance_urt(self) -> _NDArray_[_np_.float16]:
        """
        saturated float16[6] covariance_urt
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._covariance_urt

    @covariance_urt.setter
    def covariance_urt(self, x: _NDArray_[_np_.float16] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float16 and x.ndim == 1 and x.size == 6:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._covariance_urt = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float16).flatten()
            if not x.size == 6:  # Length cannot be checked before casting and flattening
                raise ValueError(f'covariance_urt: invalid array length: not {x.size} == 6')
            self._covariance_urt = x
        assert isinstance(self._covariance_urt, _np_.ndarray)
        assert self._covariance_urt.dtype == _np_.float16  # type: ignore
        assert self._covariance_urt.ndim == 1
        assert len(self._covariance_urt) == 6

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.value._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.covariance_urt) == 6, 'self.covariance_urt: saturated float16[6]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.covariance_urt)
        _ser_.pad_to_alignment(8)
        assert 288 <= (_ser_.current_bit_length - _base_offset_) <= 288, \
            'Bad serialization of reg.udral.physics.kinematics.cartesian.PointVar.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> PointVar_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.kinematics.cartesian.Point_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "covariance_urt"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float16, 6)
        assert len(_f1_) == 6, 'saturated float16[6]'
        self = PointVar_0_1(
            value=_f0_,
            covariance_urt=_f1_)
        _des_.pad_to_alignment(8)
        assert 288 <= (_des_.consumed_bit_length - _base_offset_) <= 288, \
            'Bad deserialization of reg.udral.physics.kinematics.cartesian.PointVar.0.1'
        assert isinstance(self, PointVar_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
            'covariance_urt=%s' % _np_.array2string(self.covariance_urt, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'reg.udral.physics.kinematics.cartesian.PointVar.0.1({_o_0_})'

    _EXTENT_BYTES_ = 36

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8Q-pP50{`t;TaOgS72f-W`?5fY@nvuvybu`r-qp6jIM^7u0B>w(St%mzn(1Pz*FDp%?w-|-B_#VH5lAh$Br1~sL3od3;arjJ'
        'Bs@ln6xsj4Kf#YVXQrB6VD}-<*_F1x(_N>|IaOWfJE!N9iQip0I5POFUdZ}U5hcyA;CalF_+!>ecr$FLoh&WllB;U(`(@s1m%W^S'
        '(9gKKt4@BZZmET8GVHPrjGxW<O0yT`ENNz<U&QUA`BB{E9af^)W_ihrn01?rY1}QBSgxv>aE<3hoOYEMsiv2-d{@yCI{I7nsj7B|'
        'tSs}m)q|<(2Kd@0%12tNn!FVAB-)5>R~WI9g(Ze8#)c2YWOe#~308?|F<S>E_S{h7fHpM0$>i}KTWiCVB5wA&aoJ3Gccm1~>v6=F'
        'c)Lt<duV5rjy!FrI=0Qq@|^Wmb?8#O&Z8>>i*Mkg$6vwTkSDyuyXA15+ig>p$DO#0*Fa<TQj)UraVxvSR$PX|uob-kTi0eq8FtbL'
        'w(eAQWU-!()0!7y>?#i7`}&P~4}uJfl651NN1F}Z20I<L0z1-+(DBWjwM%%<1-$=DS_T`-?&!#f=?A_S*rx3e&$3O|H;C!DmhV`$'
        'Z=1g1*skXX#PAJ3*K&#D1cB!UBrtu)_lSXWEYI+XVOYeqiSHRM30#+Ww&i;s@rmi1u46d()OJnBCYIxYdB?U)+wuqr;MOFdOdN0l'
        '|Ay__zH52`@eJ^08m{lTu4xg=@IA|Moxm^x!zO`k!DPqq!5MK4;((HE2Vfh$*_Q2rmStIiLrl*l265fM2CtS4tA!=P(uw6+hGRO8'
        '4~vIjZHU%4i4mBA6$FHsmTN%lhUJ;WF)fFHU5_Z-{9db?h1Zp_c3k!q9j_+BRsvgmqCN>5Zv+lS`Q*K-_WV39hv(~kxYcK(8V}P<'
        'RgLY86#Y&sP2#qy=CATj3g-;p=DQis8JzcxlQk8#MGRRf-l`71$1`5WTkDO5A3^Nm9njl<t(PP$??0&ow$@nE<LWcDKrhIm1uLHj'
        'J8@Uh2Pm+06sGai_7a9x=_sm>NIIr*T;qhsNyITpr}X_a;<%(U`hHg5@6vj^5ho?xqsR9m?viw$#{GzUBt4+V=d}Jo{d`{AIi&9o'
        'Yx_qK4@mkW#2HDC>iIuLoRjn!ZU30oe-`nmq|YH9l=OLR?*+suNgI0pal~VizKD24(w}I1FKPXsB2G(sLdW$o;!Bb)AT}gDiTJFf'
        'r?kJHAs&+Sw2t?Tw$s#cpGBOI)X@G-#50mwh^HjA5nq<n(SBUS<C1!a&r9m-c!~BGARd<V6}`?^5%){_n)Z7RaaPjvdfl(<{kfq1'
        'Uq&<}UDojm#AQj>5id)68<9x*IpTt(_q5;pdOZ&jA4vMG#_u)$FvP1fqgpsx3k$VCYT<G%EZ2glh4osvT??Pr!o6C!UkeXw;oDmH'
        'z7~GaLJtU+uV<_~sHXZ^3ljy3)MSU397^v*7^RT5BS0Lin%`7r!&ZM-&u=MlU%XgARfu?&^ENAar0!Jv!kbu%!Ys|pFpku<YA!6&'
        'Uf$*~knk{L!1>iQLK3%t?-!wcSYO1acOk<^&w_7}V!tp|0y5yJ@s$_|XxGJlCRp+&@Q8wH*lPi=gixg+i^20o6^98^!%C~Fu_6X@'
        'SZ(2<t~b@8O%=CkHjO57mnyMB&4+>&5Mqv{5^CdG+~(?z_)`2)oEL8l_(i-a-quBVKtqcxisJ6dQ(Oh3m!W~lhQo@^!1gZD2jV*X'
        'FYmC<4(t5Cv5xrSNvavvY0NGl8S$rEYL!5bC!Q(9U+##%UK4*4UoD8Q#W&*b;veFl;$bxo=?)$Ipe;uZ88+rX4I8aF5Xz(GTvhu9'
        '?Kz~lxsl}JUy#t%sf)E%qn)NX<S4L6(MWGLSR=zpjkwz=pk3lkwRP_Q=aKYp@!d{(@1*xmdT*cJn?8t7Xz8Rlt);W{fG~t3+}pwv'
        'K{W}VPlltvTEsazwRQeo(bBu1@Q(P!P~n5&ZVy6Oq8~y!eu(K<XJaA0xb`T(eeHCO!RK!mT9aN5AMsyS!LJ7G&#$c;jm9rCDCuYN'
        'ctw<r64h1`j{Hyx-q@Jg0NTmp^(KVMk-`>Me~%nCxB6#*)q8O1ZNp}(ub{@OczF#k=kRhKF4bK93&<A4wOuE&!A6_AlfxI&E;eS}'
        'Ex)_)ix5A%pxeP8PqwnQ`WCL{J39I}y$!Z;^$#${3mCZC7!}v?QV-RH_|yPyee=II!q&rA5&!@'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)