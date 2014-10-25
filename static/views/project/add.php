        <div class="row">
            <div class="col-lg-12 col-md-12 col-sm-8 col-xs-9 shade-container">
                <div class="col-lg-12 col-md-12 col-sm-9 col-xs-9">
                    <!-- control panel -->
                    <div class="col-lg-2">
                        <form id="new_project" method="post" enctype="multipart/form-data">
                            <!-- project name -->
                            <div class="control-group">
                                <label>Project name:</label><br />
                                <input type="text" name="projectName" placeholder="Name" class="input-xlarge" id="project_name" required>
                            </div>

                            <!-- project description -->
                            <div class="control-group">
                                <label>Project description:</label><br />
                                <textarea rows="12" placeholder="Description" id="project_des" required></textarea>
                            </div>

                            <!-- dataset selection -->
                            <label>Select Dataset:</label><br />
                            <div>
                                <select id="project_dataset" class="selectpicker" data-live-search="true" data-width="80%" required>
        							<?php foreach($datasets as $set) {
        										$dataset_id = $set['id'];
        										$dataset_name = $set['name'];?>
                                        <option value = "<?php echo $dataset_id?>"><?php echo $dataset_name?></option>
        							<?php } ?>
                                </select>
                            </div>

                            <!-- privacy selection -->
                            <div class="control-group">
                                <label>Is this a private project?</label><br />
                                <div class="radio">
                                    <label>
                                        <input type="radio" name="visability" value="yes" checked> Yes
                                    </label>
                                </div>
                                <div class="radio" id="visability_no">
                                    <label>
                                        <input type="radio" name="visability" value="no"> No
                                    </label>
                                </div>
                            </div>

                            <!-- save the project -->
                            <div class="control-group">
                                <label>Save the project?</label>
                                <div class="btn-toolbar">
                                    <button type="submit" class="btn btn-default btn-sm" id="project_save"><span class="glyphicon glyphicon-floppy-saved"></span> Save</button>
                                    <button type="button" class="btn btn-default btn-sm" id="btn_restart"><span class="glyphicon glyphicon-repeat"></span> Restart</button>
                                </div>
                            </div>
                        </form>                                                 
                    </div>

                    <!-- data view -->
                    <div class="col-lg-10">
                        <div class="row" id="main_data_preview">
                            <fieldset class="field-border">
                                <legend class="field-border">Data View</legend>
                                <div id="main_table_view">             
                                    <table id="data_view" class="display">
                                        <!-- TO DO: dynamically generate table head -->
                                        <thead>
                                            <tr>
                                                <th>Doc ID</th>
                                                <th>People</th>
                                                <th>Location</th>
                                                <th>Organization</th>
                                                <th>Phone</th>
                                                <th>Misc</th>
                                            </tr>
                                        </thead>
                                    </table>
                                </div>
                            </fieldset>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <script type="text/javascript" src="<?php echo PUBLIC_PATH?>js/lib/jquery.dataTables.min.js"></script> 
        <script type="text/javascript" src="<?php echo PUBLIC_PATH?>js/common.js"></script>
    </body>
</html>