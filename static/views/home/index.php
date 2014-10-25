        <!-- four cards for users -->
        <div class="row">
            <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">                                               
                <div class="panel panel-default shade-container">
                    <div class="panel-heading">
                        <!-- title -->
                        <h3 class="panel-title">My Dashboard</h3>
                    </div>

                    <div class="panel-body">
                        <!-- project -->
                        <div class="row">
                             <div class="col-xs-6 col-md-6">
                                <a href="<?php echo SERVER_PATH.'project/plist/'?>" class="btn btn-success btn-lg" role="button"><span class="glyphicon glyphicon-tasks"></span> <br/>Project 
                                <br/>I have <?php echo isset($projects_number)?$projects_number:'0'?> projects.</a>
                            </div>

                            <!-- dataset -->
                            <div class="col-xs-6 col-md-6">
                                <a href="<?php echo SERVER_PATH.'dataset/index/'?>" class="btn btn-warning btn-lg" role="button"><span class="glyphicon glyphicon-cog"></span> <br/>Dataset
                                <br/>I can access <?php echo isset($datasets_number)?$datasets_number:'0'?> datasets.</a>
                            </div>                           
                        </div>

                        <div class="row">
                             <!-- visualizations -->
                            <div class="col-xs-6 col-md-6">
                                <a href="<?php echo SERVER_PATH.'dataviz/index/'?>" class="btn btn-primary btn-lg" role="button"><span class="glyphicon glyphicon-eye-open"></span> <br/>Visualization
                                <br/>TO-DO</a>
                            </div>

                            <!-- user profile -->
                            <div class="col-xs-6 col-md-6">
                                <a href="<?php echo SERVER_PATH.'login/profile/'?>" class="btn btn-info btn-lg" role="button"><span class="glyphicon glyphicon-user"></span> <br/>Profile
                                <br/>TO-DO</a>
                            </div>               
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </body>
</html>