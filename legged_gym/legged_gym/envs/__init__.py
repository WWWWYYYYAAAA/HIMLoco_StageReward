# SPDX-FileCopyrightText: Copyright (c) 2021 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Copyright (c) 2021 ETH Zurich, Nikita Rudin

from legged_gym import LEGGED_GYM_ROOT_DIR, LEGGED_GYM_ENVS_DIR
from legged_gym.envs.a1.a1_config import A1RoughCfg, A1RoughCfgPPO
from .base.legged_robot import LeggedRobot
from .base.legged_robot_StageR import LeggedRobotSR
from .a1.a1_config import A1RoughCfg, A1RoughCfgPPO
from legged_gym.envs.go1.go1_config import Go1RoughCfg, Go1RoughCfgPPO
from legged_gym.envs.aliengo.aliengo_config import AlienGoRoughCfg, AlienGoRoughCfgPPO
from legged_gym.envs.zsl1.zsl1_config import ZSL1RoughCfg, ZSL1RoughCfgPPO
from legged_gym.envs.zsl1.zsl1_plane_config import ZSL1PlaneCfg, ZSL1PlaneCfgPPO

import os

from legged_gym.utils.task_registry import task_registry

task_registry.register( "a1", LeggedRobot, A1RoughCfg(), A1RoughCfgPPO() )
task_registry.register( "go1", LeggedRobot, Go1RoughCfg(), Go1RoughCfgPPO() )
task_registry.register( "aliengo", LeggedRobot, AlienGoRoughCfg(), AlienGoRoughCfgPPO() )
task_registry.register( "zsl1", LeggedRobot, ZSL1RoughCfg(), ZSL1RoughCfgPPO() )
task_registry.register( "zsl1SR", LeggedRobotSR, ZSL1PlaneCfg(), ZSL1PlaneCfgPPO() )

