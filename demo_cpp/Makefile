CINCLUDES += ./libcanard/libcanard/
CINCLUDES += ./includes/reg/udral/service/sensor
CINCLUDES += ./includes/reg/udral/service/common
CINCLUDES += ./includes/reg/udral/service/battery
CINCLUDES += ./includes/reg/udral/service/actuator/servo
CINCLUDES += ./includes/reg/udral/service/actuator/esc
CINCLUDES += ./includes/reg/udral/service/actuator/common/sp
CINCLUDES += ./includes/reg/udral/physics/time
CINCLUDES += ./includes/reg/udral/physics/thermodynamics
CINCLUDES += ./includes/reg/udral/physics/optics
CINCLUDES += ./includes/reg/udral/physics/kinematics/translation
CINCLUDES += ./includes//reg/udral/physics/kinematics/rotation
CINCLUDES += ./includes/reg/udral/physics/kinematics/
CINCLUDES += ./includes/reg/udral/physics/electricity
CINCLUDES += ./includes/reg/udral/physics/dynamics/translation
CINCLUDES += ./includes/reg/udral/physics/dynamics/rotation
CINCLUDES += ./includes/reg/udral/physics/acoustics
CINCLUDES += ./includes/uavcan/pnp/cluster
CINCLUDES += ./includes/uavcan/si/unit/angular_acceleration
CINCLUDES += ./includes/uavcan/file
CINCLUDES += ./includes/uavcan/si/unit/frequency
CINCLUDES += ./includes/uavcan/diagnostic
CINCLUDES += ./includes/uavcan/primitive/array
CINCLUDES += ./includes/uavcan/si/unit/force
CINCLUDES += ./includes/uavcan/si/unit/angle
CINCLUDES += ./includes/uavcan/si/unit/duration
CINCLUDES += ./includes/uavcan/node/port
CINCLUDES += ./includes/uavcan/_register
CINCLUDES += ./includes/uavcan/si/unit/electric_current
CINCLUDES += ./includes/uavcan/si
CINCLUDES += ./includes/uavcan/si/unit/angular_velocity
CINCLUDES += ./includes/uavcan/si/unit/length
CINCLUDES += ./includes/uavcan/pnp
CINCLUDES += ./includes/uavcan/si/unit/acceleration
CINCLUDES += ./includes/uavcan/primitive
CINCLUDES += ./includes/uavcan/node
CINCLUDES += ./includes/uavcan/si/unit/energy
CINCLUDES += ./includes/uavcan/metatransport/can
CINCLUDES += ./includes/uavcan/si/unit/electric_charge
CINCLUDES += ./includes/uavcan/primitive/scalar
CINCLUDES += ./includes/uavcan/si/unit/magnetic_field_strength
CINCLUDES += ./includes/uavcan/si/unit/mass
CINCLUDES += ./includes/uavcan/si/unit/power
CINCLUDES += ./includes/uavcan/si/unit/pressure
CINCLUDES += ./includes/uavcan/si/unit/temperature
CINCLUDES += ./includes/uavcan/si/unit/torque
CINCLUDES += ./includes/uavcan/si/unit/velocity
CINCLUDES += ./includes/uavcan/si/unit/voltage
CINCLUDES += ./includes/uavcan/si/unit/volume
CINCLUDES += ./includes/uavcan/si/unit/volumetric_flow_rate
CINCLUDES += ./includes/uavcan/time
CINCLUDES += ./includes/


INCDIR   := $(patsubst %, -I%,$(CINCLUDES))


CSOURCES += ./libcanard/libcanard/canard.c
CPPSOURCES += cyphal_demo.cpp
CPPSOURCES += CyphalReceive.cpp

COBJS = $(CSOURCES:%.c=%.o)
CPPOBJS = $(CPPSOURCES:%.cpp=%.o)

all:
	gcc -c $(INCDIR) $(CSOURCES)
	g++ -pthread -c $(INCDIR) $(CPPSOURCES)
	g++ -pthread -o  cyphal_demo canard.o $(CPPOBJS)


clean:
	rm -rf build