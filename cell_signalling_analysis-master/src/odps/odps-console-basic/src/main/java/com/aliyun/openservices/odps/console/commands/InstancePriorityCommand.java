/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

package com.aliyun.openservices.odps.console.commands;

import java.util.List;

import com.aliyun.odps.OdpsException;
import com.aliyun.odps.utils.StringUtils;
import com.aliyun.openservices.odps.console.ExecutionContext;
import com.aliyun.openservices.odps.console.ODPSConsoleException;
import com.aliyun.openservices.odps.console.utils.ODPSConsoleUtils;

/**
 * @author shuman.gansm
 * */
public class InstancePriorityCommand extends AbstractCommand {

  int priority = 9;

  public InstancePriorityCommand(int priority, String commandText, ExecutionContext context) {
    super(commandText, context);
    this.priority = priority;
  }

  public void run() throws OdpsException, ODPSConsoleException {

    getContext().setPriority(priority);
  }

  /**
   * 通过传递的参数，解析出对应的command
   * **/
  public static InstancePriorityCommand parse(List<String> optionList,
      ExecutionContext sessionContext) throws ODPSConsoleException {

    String instancePriorty = ODPSConsoleUtils.shiftOption(optionList, "--instance-priority");

    if (!StringUtils.isNullOrEmpty(instancePriorty)) {

      int priority;
      try {
        priority = Integer.parseInt(instancePriorty.trim());
      } catch (NumberFormatException e) {
        throw new ODPSConsoleException("priority need int value[--instance_priority="
            + instancePriorty + "]");
      }

      return new InstancePriorityCommand(priority, "--instance-priority", sessionContext);
    }

    return null;
  }
}
